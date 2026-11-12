"""Busca única: os provedores são detalhes de integração, não etapas do cadastro."""
from dataclasses import asdict,replace
from .automatic_catalog import normalized,best_match
from .integrations import MetadataResult,IntegrationError
from .integrations.steam_store import SteamStoreProvider


def providers():
    from .integrations.http import HttpClient
    sources={'steam':SteamStoreProvider(HttpClient(timeout=8,attempts=1))}
    from .credentials import CredentialVault
    from .integrations.metadata import RawgProvider,SteamGridDbProvider
    for name,factory in [('rawg',RawgProvider),('steamgriddb',SteamGridDbProvider)]:
        try:
            key=CredentialVault().get(name)
            if key:sources[name]=factory(key,HttpClient(timeout=8,attempts=1))
        except Exception:continue
    return sources


def search_titles(title,platform='',sources=None):
    sources=providers() if sources is None else sources
    results=[];failed=0
    from concurrent.futures import ThreadPoolExecutor
    active=[(name,provider) for name,provider in sources.items() if not (name=='steam' and platform and normalized(platform) not in {'pc','windows'})]
    with ThreadPoolExecutor(max_workers=max(1,len(active))) as pool:
        pending=[(name,pool.submit(provider.search,title)) for name,provider in active]
        for name,future in pending:
            try:
                found=future.result()
                for result in found:
                    if platform and result.platforms and best_match(result.title,platform,[result]) is None:continue
                    merged=False
                    for index,previous in enumerate(results):
                        identities={**previous.identifiers,previous.provider:previous.external_id}
                        known=identities.get(result.provider)
                        if known and known!=result.external_id:continue
                        if normalized(previous.title)!=normalized(result.title):continue
                        if previous.release_date and result.release_date and previous.release_date[:4]!=result.release_date[:4]:continue
                        if previous.platforms and result.platforms and not set(previous.platforms)&set(result.platforms):continue
                        identities.update({**result.identifiers,result.provider:result.external_id})
                        results[index]=replace(previous,identifiers=identities,
                            platforms=tuple(dict.fromkeys([*previous.platforms,*result.platforms])),
                            release_date=previous.release_date or result.release_date)
                        merged=True;break
                    if not merged:results.append(result)
            except Exception:failed+=1
    results.sort(key=lambda row:(normalized(row.title)!=normalized(title),not bool(row.platforms)))
    return {'results':[asdict(row) for row in results[:24]],'unavailable':failed}


def selected_details(provider,identity,platform='',sources=None):
    sources=providers() if sources is None else sources
    if provider not in sources:raise IntegrationError('Catálogo indisponível. Você pode adicionar o jogo e tentar completar a ficha depois.')
    source=sources[provider]
    result=source.details(identity) if hasattr(source,'details') else source.game_by_id(identity)
    if result.provider!=provider or result.external_id!=identity:raise IntegrationError('O catálogo retornou outro jogo. Seleção preservada.')
    identities={**result.identifiers,provider:identity}
    # Complementa automaticamente a ficha e as artes, preservando edição/plataforma.
    for name,other in sources.items():
        if name==provider:continue
        if name=='steam' and platform and normalized(platform) not in {'pc','windows'}:continue
        try:
            match=best_match(result.title,platform,other.search(result.title))
            if not match or normalized(match.title)!=normalized(result.title):continue
            detail=other.details(match.external_id) if hasattr(other,'details') else match
            if normalized(detail.title)!=normalized(result.title):continue
            identities[name]=detail.external_id
            result=replace(result,description=result.description or detail.description,
                developer=result.developer or detail.developer,publisher=result.publisher or detail.publisher,
                release_date=result.release_date or detail.release_date,genres=result.genres or detail.genres,
                platforms=result.platforms or detail.platforms,images={**detail.images,**result.images})
        except Exception:continue
    return replace(result,identifiers=identities)


def preview_details(database,provider,identity,platform=''):
    sources=providers();result=selected_details(provider,identity,platform,sources)
    from .integrations.images import ImageCache
    from pathlib import Path
    cache=ImageCache(Path(database).parent/'images',timeout=8);preview={}
    for kind in ('cover','banner'):
        candidates=[]
        art_identity=result.identifiers.get('steamgriddb') or (identity if provider=='steamgriddb' else None)
        if art_identity and 'steamgriddb' in sources:
            try:candidates=sources['steamgriddb'].artworks(art_identity,kind)[:2]
            except Exception:pass
        candidates+=([result.images[kind]] if result.images.get(kind) else [])
        candidates+=result.image_candidates.get(kind,[])
        for url in candidates[:2]:
            try:preview[kind]=cache.download(url);break
            except (IntegrationError,OSError,ValueError):continue
    return {'result':asdict(result),'preview':preview}

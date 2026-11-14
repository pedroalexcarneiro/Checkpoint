"""Resumo de apresentação; não participa da busca nem altera o texto armazenado."""
import re


def intro(value):
    paragraph=re.split(r'\n\s*\n|\n(?=[*#=•-])',value.strip(),maxsplit=1)[0]
    paragraph=re.sub(r'\([^)]*\d[^)]*\)','',paragraph)
    paragraph=re.sub(r'\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}(?:º)?\s+de\s+[a-zç]+\s+de\s+\d{4}\b|\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b','',paragraph,flags=re.I)
    paragraph=re.sub(r'\b(?:1[0-9]{3}|20[0-9]{2})\b','',paragraph)
    sentences=[]
    for sentence in re.split(r'(?<=[.!?])\s+',paragraph):
        if re.search(r'\b(história|vers(?:ão|ões)|listas?|relançamento|remaster|remake)\b',sentence,re.I):continue
        sentence=re.sub(r'\s+',' ',sentence).strip()
        sentence=re.sub(r'\s+([.,;!?])',r'\1',sentence)
        sentence=re.sub(r'\s+(?:em|desde|no ano de)\s*([.!?])',r'\1',sentence)
        if sentence:sentences.append(sentence)
        if len(sentences)==3:break
    return ' '.join(sentences)

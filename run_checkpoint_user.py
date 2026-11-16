"""Variante portátil que usa somente os privilégios atuais do usuário."""
from checkpoint.app import main

raise SystemExit(main(request_elevation=False))

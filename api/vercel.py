# api/vercel.py
import os, sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

# adiciona raiz e /server no PYTHONPATH
for p in (ROOT_DIR, ROOT_DIR / "server"):
    sp = str(p)
    if sp not in sys.path:
        sys.path.append(sp)

# Aponta para o settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.config.settings")

from django.core.asgi import get_asgi_application
app = get_asgi_application()


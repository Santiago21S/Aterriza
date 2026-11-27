#!/usr/bin/env bash
# Instala todo lo necesario para arrancar la base por primera vez.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PYTHON="${PYTHON:-python3}"

echo "==> Creando entorno virtual en .venv"
"$PYTHON" -m venv .venv

echo "==> Instalando dependencias de Python"
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r backend/requirements.txt

echo "==> Aplicando migraciones de Django"
(cd backend && "$ROOT/.venv/bin/python" manage.py migrate)

echo "==> Instalando dependencias de Node"
if command -v npm >/dev/null 2>&1; then
  (cd frontend && npm install)
else
  (cd frontend && yarn install)
fi

echo
echo "Todo listo. Arranca la aplicación con:"
echo "  ./scripts/dev.sh"
echo
echo "Después abre http://localhost:3000"

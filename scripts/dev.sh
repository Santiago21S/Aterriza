#!/usr/bin/env bash
# Arranca Django (8000) y el frontend Node (3000) a la vez.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ ! -x .venv/bin/python ]; then
  echo "No existe .venv. Ejecuta primero: ./scripts/setup.sh"
  exit 1
fi

if [ ! -d frontend/node_modules ]; then
  echo "Faltan las dependencias de Node. Ejecuta primero: ./scripts/setup.sh"
  exit 1
fi

pids=()

cleanup() {
  trap - EXIT INT TERM
  for pid in "${pids[@]}"; do
    kill "$pid" 2>/dev/null || true
  done
  wait 2>/dev/null || true
}
trap cleanup EXIT INT TERM

echo "==> Django en http://127.0.0.1:8000"
(cd backend && "$ROOT/.venv/bin/python" manage.py runserver 127.0.0.1:8000) &
pids+=($!)

echo "==> Frontend en http://localhost:3000"
(cd frontend && node server.js) &
pids+=($!)

echo
echo "Abre http://localhost:3000 (Ctrl+C para parar todo)"
echo

wait -n "${pids[@]}"

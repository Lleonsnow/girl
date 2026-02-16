#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m django startproject config .
echo "Done. Activate venv: source .venv/bin/activate"

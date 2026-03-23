#!/usr/bin/env sh
set -e

cd /app/backend
pytest app/tests -q

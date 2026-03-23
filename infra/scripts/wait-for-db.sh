#!/usr/bin/env sh
set -e

host="${1:-db}"
port="${2:-5432}"

until nc -z "$host" "$port"; do
  echo "Waiting for database at $host:$port"
  sleep 1
done

echo "Database is ready"

#!/usr/bin/env bash

set -o errexit
set -o pipefail

cmd="$@"

cd /app

exec python manage.py $cmd

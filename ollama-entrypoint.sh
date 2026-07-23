#!/bin/sh
# start ollama, wait until it's ready and pull the required model

set -e

ollama serve &
pid=$!

until ollama list >/dev/null 2>&1; do
    sleep 1
done

ollama pull llama3.2:3b

wait "$pid"
#!/bin/sh
# start ollama, wait until it's ready and pull the required model

set -e

ollama serve &
pid=$!

until ollama list >/dev/null 2>&1; do
    sleep 1
done

ollama pull qwen3:0.6b

wait "$pid"
# agent-email-router

AI agent message routing to department email, using FastAPI, Pydantic AI, Ollama and MailHog.

## Run

Clone the repository:

```bash
git clone https://github.com/feegloo/agent-email-router.git
cd agent-email-router
```

Start the application:

```bash
docker compose up -d --wait
```

The first start may take longer because Ollama needs to download the model.

Services:

- API: http://localhost:8000
- Swagger: http://localhost:8000/api/v1/docs
- MailHog: http://localhost:8025

## Test

```bash
curl -X POST http://localhost:8000/api/v1/user-messages \
  -H "Content-Type: application/json" \
  -d '{
    "email": "adam.nowak@example.com",
    "message": "Mam problem z antywirusem"
  }'
```

```bash
curl -X POST http://localhost:8000/api/v1/user-messages \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jak.kowalski@example.com",
    "message": "Chciałbym zgłosić urlop na jutro"
  }'
```

```bash
curl -X POST http://localhost:8000/api/v1/user-messages \
  -H "Content-Type: application/json" \
  -d '{
    "email": "adam.nowak@example.com",
    "message": "Chciałbym umówić się na podpisanie umowy"
  }'
```

```bash
curl -X POST http://localhost:8000/api/v1/user-messages \
  -H "Content-Type: application/json" \
  -d '{
    "email": "adam.nowak@example.com",
    "message": "gdzie jest parking w biurze?"
  }'
```

```bash
curl -X POST http://localhost:8000/api/v1/user-messages \
  -H "Content-Type: application/json" \
  -d '{
    "email": "adam.nowak@example.com",
    "message": "test"
  }'
```

The API returns `202 Accepted`. The routed email should appear in MailHog within approximately 10–60 seconds.

## Model

The default model is:

```text
qwen3.5:0.8b
```

The model runs locally using Ollama.

### Known issues

- The model may occasionally fail to call the required tool.
- The model may occasionally call the tool with invalid arguments.

## Local API development

Rebuild and start after code changes:

```bash
docker compose up -d --wait --build
```

You can also run the API without `api` Docker container.

Create the local environment file:

```bash
cp .env.example .env
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -e .
```

Run the API with code livereload:

```bash
make dev
```
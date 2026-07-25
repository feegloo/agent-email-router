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

The `--wait` flag waits until required services are ready. 
The API starts only after Ollama initialization completes, and Docker Compose waits until the API reports healthy status by responding to `/health` endpoint.

Services:

- API: http://localhost:8000
- Swagger: http://localhost:8000/api/v1/docs
- MailHog: http://localhost:8025


## Test

API endpoint:

```
POST /api/v1/user-messages
```

returns `HTTP 202 Accepted` with JSON response `{"message": "processing"}`

The message is processed using a FastAPI background task, so the HTTP request does not wait for the LLM and email delivery to finish.

The routed email should appear in MailHog within approximately 10–60 seconds.

Example curl commands to send messages that the Agent routes to the appropriate department:

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
# agent-email-router

AI agent message routing to department email, using FastAPI, Pydantic AI, Ollama, MailHog and Docker.

For example, when the user `adam.nowak@example.com` sends the message `"Chciałbym wziąć jutro urlop"`, the Agent sends an email from `agent-email-router@example.com` to `kadry@example.com`, with the `Reply-To` header set to `adam.nowak@example.com`. The email can then be previewed in MailHog.

The email routing addresses are configured through environment variables in [docker-compose.yml](./docker-compose.yml)

```
EMAIL_FROM: agent-email-router@example.com
EMAIL_HUMAN_RESOURCES: human-resources@example.com
EMAIL_HELP_DESK: help-desk@example.com
EMAIL_IT: it@example.com
EMAIL_KADRY: kadry@example.com
EMAIL_OTHER: other@example.com
```

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

In CPU mode, the first routed email should appear in MailHog within 60 seconds, as the model needs time to initialize.

Subsequent messages should appear within approximately 10–30 seconds.

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

```
qwen3.5:0.8b
```

The model runs locally using Ollama.

It's the lightest and fastest Qwen 3.5 model that supports tool use while maintaining a relatively low error rate.

#### Known issues

- The model may occasionally fail to call the required tool.
- The model may occasionally call the tool with invalid arguments.

Another model I tested was `qwen3.5:1.7b`, which could reduce the error rate, but its CPU inference was too slow for the purposes of the demo.

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

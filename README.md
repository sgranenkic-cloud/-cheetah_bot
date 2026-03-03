# Cheetah.Club Telegram Bot (Railway via Docker)

## Deploy (Railway)
1. Push this repo to GitHub.
2. Railway → New Project → Deploy from GitHub Repo.
3. Set Variables:
   - `BOT_TOKEN` = token from @BotFather
4. Deploy.

This repo includes a `Dockerfile`, so Railway will build a Docker image.

## Local run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN="YOUR_TOKEN"
python bot.py
```

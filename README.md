# Cheetah.Club Telegram Bot (Railway)

Simple info bot with 4 menu buttons + nested actions for joining the club.

## Features
- /start greeting message
- Persistent reply-keyboard menu:
  - Стать настоящим гепардом
  - Что нужно, чтобы начать бегать?
  - Где проходят занятия
  - Какая стоимость занятий
- "Стать настоящим гепардом" shows inline buttons:
  - Написать тренеру (opens chat with @grondkind)
  - Заполнить форму (Yandex form link)

## Setup

### 1) Create a bot token
Create a bot via @BotFather and copy the token.

### 2) Deploy on Railway
- Push this repo to GitHub
- In Railway: **New Project → Deploy from GitHub Repo**
- Add environment variable:
  - `BOT_TOKEN` = your token
- Deploy

Railway will build using the included `Dockerfile`.

## Local run (optional)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN="YOUR_TOKEN"
python bot.py
```

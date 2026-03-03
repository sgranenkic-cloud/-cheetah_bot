# Telegram Bot (Railway Ready)

## Deployment (Railway)

1. Upload this project.
2. Settings → Variables → Add:
   BOT_TOKEN=your_telegram_bot_token
3. Scaling → Replicas = 1
4. Deploy.

## Important
- Polling only (no webhook).
- Always keep replicas = 1.

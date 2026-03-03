FROM python:3.11-slim

WORKDIR /app

# Ensure pip exists and is up to date
RUN python -m ensurepip --upgrade && python -m pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]

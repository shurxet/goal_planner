FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
COPY entrypoint.sh .

CMD ["sh", "entrypoint.sh"]

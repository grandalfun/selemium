FROM python:3.10-slim

WORKDIR /_data

COPY bot.py .

RUN pip install selenium

CMD ["python", "bot.py"]

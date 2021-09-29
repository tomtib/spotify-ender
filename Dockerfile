FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
ADD . .

CMD python3 downloader.py


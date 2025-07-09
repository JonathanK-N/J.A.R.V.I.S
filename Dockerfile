FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    portaudio19-dev \
    libasound2-dev \
    tesseract-ocr \
    libtesseract-dev \
    ffmpeg \
    libsm6 libxext6 libxrender-dev \
    python3-opencv \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "jarvis.py"]


FROM python:3.11-slim
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && \
    python -m nltk.downloader punkt wordnet omw-1.4

EXPOSE 5000
CMD ["python", "app.py"]

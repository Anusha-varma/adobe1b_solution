
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY requirements.txt .
# Install dependencies and force compatible versions
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install huggingface_hub==0.14.1 sentence-transformers==2.2.2

COPY . .

CMD ["python", "main.py"]


FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY validation.py .
COPY tests/ ./tests/
COPY pytest.ini .

CMD ["python", "-m", "pytest", "tests/", "-v", "-m", "not integration"]

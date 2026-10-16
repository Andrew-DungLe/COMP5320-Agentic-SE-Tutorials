FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt
COPY . .
ENV PYTHONPATH=/app/src
CMD ["sh", "-c", "python -m pytest -q && python -m demo_app.core"]

FROM python:3.14-slim

WORKDIR /workspace
COPY pyproject.toml .
COPY *.py .
RUN pip install --no-cache-dir .

CMD ["python", "./container_loop.py"]

# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
# copy requirements first (for cache optimization)
COPY app/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
# copy application code
COPY app/ .
# Stage 2: Final image
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

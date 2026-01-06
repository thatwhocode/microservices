FROM python:3.12-bookworm
WORKDIR /app

COPY auth_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
CMD ["uvicorn", "auth_service.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
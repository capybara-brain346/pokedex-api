FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./api /app/api

EXPOSE 8080

CMD ["fastapi", "run", "api/main.py", "--port", "8080"]
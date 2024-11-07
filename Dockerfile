FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install "fastapi[standard]"

RUN pip install psycopg2-binary

COPY ./api /app/api

COPY pokemon.db /app/

EXPOSE 8080

CMD ["fastapi", "run", "api/main.py", "--port", "8080"]
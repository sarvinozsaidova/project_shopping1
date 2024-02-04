FROM --platform=linux/amd64 python:3.10  as builder

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

FROM --platform=linux/amd64 python:3.11

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"

COPY --from=builder /opt/venv /opt/venv

COPY . .

EXPOSE 8000

RUN pip install uvicorn

CMD python manage.py collectstatic  --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    uvicorn shopping.asgi:application --host 0.0.0.0 --port 8000
FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /app/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        fastapi-user

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD python main.py
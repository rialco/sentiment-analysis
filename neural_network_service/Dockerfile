FROM python:3.10.4-alpine3.15

RUN apk add --no-cache bash

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install redis

COPY . .

CMD ["python", "-u", "app.py"]
FROM python:3.9.13-slim

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install redis
RUN pip install keras
RUN pip install nltk
RUN pip install numpy
RUN pip install tensorflow

COPY . .

CMD ["python", "-u", "app.py"]
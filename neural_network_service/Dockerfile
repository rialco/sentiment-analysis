FROM python:3.9-slim

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get -y update \
    && apt install -y build-essential libpq-dev

RUN pip install --upgrade pip
RUN pip install redis
# RUN pip install keras
RUN pip install nltk
RUN pip install numpy
RUN pip install pandas
RUN pip install sqlalchemy
# x86_64
# RUN pip install tensorflow
# RUN pip install psycopg2-binary
# aarch64
RUN pip install tensorflow-aarch64 -f https://tf.kmtea.eu/whl/stable.html
RUN pip install psycopg2
# Next lines are the solution for weird and sudden Type error on tensorflow imports
RUN pip uninstall --yes protobuf
RUN pip install --no-binary protobuf protobuf

COPY . .

CMD ["python", "-u", "app.py"]
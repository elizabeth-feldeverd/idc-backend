FROM python:3.8.12-buster

COPY model.h5 /model.h5
COPY idc /idc
COPY app /app
COPY pyproject.toml /pyproject.toml
COPY poetry.lock /poetry.lock
COPY steady-atlas-328003-744d53dd36cc.json /credentials.json

RUN pip install --upgrade pip
RUN pip install "poetry==1.2.2"
RUN poetry config virtualens.create false \
    && poetry install --no-interaction --noansi

CMD uvicorn app.fast:app --host 0.0.0.0 --port $PORT

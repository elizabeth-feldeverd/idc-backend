FROM python:3.8.12-buster

COPY model.h5 /model.h5
COPY idc /idc
COPY app /app
COPY requirements.txt /requirements.txt
COPY steady-atlas-328003-744d53dd36cc.json /credentials.json

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app.fast:app --host 0.0.0.0 --port $PORT

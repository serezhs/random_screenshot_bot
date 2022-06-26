FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

CMD ["python", "scr.py" ]
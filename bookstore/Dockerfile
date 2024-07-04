FROM python:3.10.12-slim

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--reload"]
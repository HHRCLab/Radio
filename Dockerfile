FROM python:3.10.7-alpine3.15

WORKDIR /app_on_docker

COPY . /app_on_docker

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
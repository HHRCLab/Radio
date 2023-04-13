FROM python:3.10.7-alpine3.15

WORKDIR /app_on_docker

COPY . /app_on_docker

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 5000
EXPOSE 5050
EXPOSE 50000
EXPOSE 50001

CMD [ "python3", "main.py" ]
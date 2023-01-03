FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn -y
RUN pip3 install flask

WORKDIR /app

COPY . /app

RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt



CMD [ "gunicorn", "-b", ":8000", "app:app" ]
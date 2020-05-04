FROM python:3.6
MAINTAINER Dinko Pehar <dinko.pehar.dev@gmail.com>

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV FLASK_APP=aukcija
EXPOSE 5000
ENTRYPOINT ["flask", "run"]
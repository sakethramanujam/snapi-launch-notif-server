FROM ubuntu:18.04
MAINTAINER saketh <ramanujamsamavedam@hotmail.com>

ENV SNAPI_DATABASE=""
ENV SNAPI_DB_HOST=""

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && apt-get -y install cron
RUN apt-get -y install python3-pip
RUN apt-get install -y software-properties-common


COPY update_crontab /etc/cron.d/update_db
RUN chmod 0644 /etc/cron.d/update_db
RUN crontab /etc/cron.d/update_db

COPY . ./app/src
RUN pip3 install --no-cache-dir -r ./app/src/requirements.txt

RUN chmod +x ./app/src/update_db.py


RUN echo "export SNAPI_DATABASE=$SNAPI_DATABASE" > /etc/environment
RUN echo "export SNAPI_DB_HOST=$SNAPI_DB_HOST" > /etc/environment
CMD ["cron","-f"]

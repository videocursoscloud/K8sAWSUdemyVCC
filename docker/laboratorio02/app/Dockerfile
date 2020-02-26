FROM ubuntu:18.04

ADD . /srv

RUN apt-get update 
RUN apt install python-pip libmysqlclient-dev python-dev -y
RUN pip install -r /srv/requirements.txt

EXPOSE 5000

CMD /usr/bin/python /srv/app.py

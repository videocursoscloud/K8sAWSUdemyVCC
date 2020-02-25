FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install nginx -y
RUN echo 'hello world' > /var/www/html/index.html

CMD nginx -g 'daemon off;'

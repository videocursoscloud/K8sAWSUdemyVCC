FROM ubuntu:18.04
 
RUN apt-get update
RUN apt-get install nginx -y
RUN apt-get install supervisor -y
RUN echo 'hello world 4.0' > /var/www/html/index.html

ADD supervisor_services.conf /etc/supervisor/conf.d/

EXPOSE 80

CMD supervisord -n -c /etc/supervisor/supervisord.conf

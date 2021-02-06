FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /home/andres/dev/flask-demo/web/app/static
COPY ./requirements.txt /home/andres/dev/flask-demo/web/requirements.txt
RUN pip3 install -r /home/andres/dev/flask-demo/web/requirements.txt

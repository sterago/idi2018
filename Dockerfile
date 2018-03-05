FROM python:2.7-stretch

RUN pip install selenium needle pytest-needle
RUN pip install -e git+https://github.com/sterago/pytest-flask.git@custom_live_server_address#egg=pytest-flask
RUN apt-get update && apt-get install perceptualdiff -y
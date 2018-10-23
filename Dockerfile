FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
RUN mkdir /src/requirements
WORKDIR /src
ADD requirements.txt /src/requirements/
RUN pip install -r /src/requirements/requirements.txt
ADD . /src/
ADD templates/ /src/templates
ADD static/ /src/static


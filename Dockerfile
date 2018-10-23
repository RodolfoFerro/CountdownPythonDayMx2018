FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD src/ /src/
RUN pip install -r /src/requirements/base.txt


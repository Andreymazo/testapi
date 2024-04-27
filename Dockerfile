FROM python:3.10.5
WORKDIR /testrestapi
EXPOSE 8000
COPY . /testrestapi
COPY ./requirements.txt .
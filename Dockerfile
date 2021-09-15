# syntax=docker/dockerfile:1

FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 80
CMD [ "python", "app2.py" ]

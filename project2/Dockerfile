FROM python:3.10.1-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install -U pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
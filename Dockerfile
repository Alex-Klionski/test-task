FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/requirements.txt

# install psycopg2 dependencies
RUN apt-get update
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

RUN pip install -r /usr/src/requirements.txt


# COPY ./entrypoint.sh .

COPY . /usr/src/app

EXPOSE 8000

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


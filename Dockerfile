FROM python:3.8-slim-buster

RUN mkdir /portfolio-team4
COPY requirements.txt /portfolio-team4
WORKDIR /portfolio-team4
RUN pip3 install -r requirements.txt

COPY . /portfolio-team4

CMD ["gunicorn", "wsgi:app", "-w 1", "-b 0.0.0.0:80"]

FROM python:3.9-slim-buster

RUN pip install pipenv
COPY Pipfile /usr/src/Pipfile
WORKDIR /usr/src

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY app /usr/src/app
COPY config.ini /usr/src/config.ini

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

CMD ["python", "app/app.py"]

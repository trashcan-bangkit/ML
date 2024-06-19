FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR /app
COPY . ./

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
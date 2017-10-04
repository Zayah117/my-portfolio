FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

# RUN export FLASK_APP=main.py

EXPOSE 5000

ENV NAME World

CMD ["python", "main.py"]

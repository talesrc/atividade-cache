FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
COPY . /app/
RUN pip install -r requirements.txt
WORKDIR  /app/basicapp/
CMD python manage.py runserver 0.0.0.0:8000
FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
COPY . /app/
RUN pip install -r requirements.txt
WORKDIR  /app/luizalabs/
#mudando a porta para não dar choque com a usada no front
CMD python manage.py runserver 0.0.0.0:8001 
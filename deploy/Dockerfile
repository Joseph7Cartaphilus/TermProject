FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python src/manage.py test && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
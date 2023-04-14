from src.myweb.celery import app
from django.core.mail import EmailMessage, send_mail

from .service import send

@app.task
def send_password_reset_email(email, url):
    message = EmailMessage(
        subject='Reset your password',
        body='Click the following link to reset your password: {}'.format(url),
        to=[email]
    )
    message.send()


@app.task
def send_spam_email(user_email):
    send(user_email)

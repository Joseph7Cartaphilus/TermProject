from celery import shared_task

from src.myweb.celery import app


def write_file(email):
    send(email)
    return True

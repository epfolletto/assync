from celery import Celery
from time import sleep

app = Celery(
    'tasks',
    broker='redis://localhost//',
    backend='redis://localhost:6379/0',
)


@app.task
def classifica(letra):
    sleep(2)
    if letra == 'a':
        return 'abacaxi'
    if letra == 'b':
        return 'banana'
    if letra == 'c':
        return 'cereja'
    if letra == 'd':
        return 'damasco'
    if letra == 'e':
        return 'embaubara'

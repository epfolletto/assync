from celery import Celery
from time import sleep

app = Celery(
    'tasks',
    broker='redis://localhost//',
    backend='redis://localhost:6379/0',
)


@app.task
def tarefa1():
    sleep(2)
    print("Tarefa 1 executada")
    return "Resultado da Tarefa 1"


@app.task
def tarefa2(resultado_tarefa1):
    sleep(2)
    print("Tarefa 2 executada:")
    print("Resultado que chegou aqui da tarefa 1:", resultado_tarefa1)
    return "Resultado da Tarefa 2"


@app.task
def tarefa3(resultado_tarefa2):
    sleep(2)
    print("Tarefa 3 executada:")
    print("Resultado que chegou aqui da tarefa 2:", resultado_tarefa2)
    return "Resultado da Tarefa 3"

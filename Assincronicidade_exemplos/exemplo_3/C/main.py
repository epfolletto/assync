from tasks import tarefa1, tarefa2, tarefa3
from celery import chain
import time

start_time = time.time()

chain(tarefa1.s(), tarefa2.s(), tarefa3.s())()

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

import time
from time import sleep


def tarefa1():
    sleep(5)
    print('estou dentro da tarefa1')


def tarefa2():
    sleep(5)
    print('estou dentro da tarefa2')


def tarefa3():
    sleep(5)
    print('estou dentro da tarefa3')


start_time = time.time()

tarefa1()
tarefa2()
tarefa3()

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

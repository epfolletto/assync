import time
from time import sleep
import threading


def tarefa1():
    sleep(5)
    print('estou dentro da tarefa1')


def tarefa2():
    sleep(5)
    print('estou dentro da tarefa2')


def tarefa3():
    sleep(5)
    print('estou dentro da tarefa3')


t1 = threading.Thread(target=tarefa1, name=tarefa1)
t2 = threading.Thread(target=tarefa2, name=tarefa2)
t3 = threading.Thread(target=tarefa3, name=tarefa3)

start_time = time.time()

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

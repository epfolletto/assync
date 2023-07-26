import time
from time import sleep
import multiprocessing

start_time = time.time()


def tarefa1():
    sleep(5)
    print('estou dentro da tarefa1')


def tarefa2():
    sleep(5)
    print('estou dentro da tarefa2')


def tarefa3():
    sleep(5)
    print('estou dentro da tarefa3')


if __name__ == '__main__':
    cod1 = multiprocessing.Process(target=tarefa1)
    cod2 = multiprocessing.Process(target=tarefa2)
    cod3 = multiprocessing.Process(target=tarefa3)

    cod1.start()
    cod2.start()
    cod3.start()
    cod1.join()
    cod2.join()
    cod3.join()

    print('estou neste ponto!')

    print('-----------------------------------------------------------')
    print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
    print('-----------------------------------------------------------')

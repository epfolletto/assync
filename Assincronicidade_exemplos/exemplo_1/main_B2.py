import time
import concurrent.futures
from time import sleep

start_time = time.time()


def tarefas(num):
    sleep(5)
    return f'estou dentro da tarefa{num}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    nums = [1, 2, 3]
    cods = executor.map(tarefas, nums)

    for cod in cods:
        print(cod)

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

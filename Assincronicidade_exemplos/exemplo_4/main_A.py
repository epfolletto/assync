import time


def tarefa1():
    print('Iniciei a tarefa 1')
    time.sleep(2)
    print('Finalizei a tarefa 1')


def tarefa2():
    print('Iniciei a tarefa 2')
    time.sleep(2)
    print('Finalizei a tarefa 2')


def tarefa3():
    print('Iniciei a tarefa 3')
    time.sleep(2)
    print('Finalizei a tarefa 3')


def main():
    tarefa1()
    tarefa2()
    tarefa3()


start_time = time.time()

main()

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

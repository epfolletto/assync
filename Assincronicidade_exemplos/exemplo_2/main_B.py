import time
import threading


def calcula_soma():
    print('Iniciando a função...')
    soma = 0
    for _ in range(300_000_000):
        soma = soma + 1
    print('Cálculo finalizado.')


if __name__ == '__main__':
    t1 = threading.Thread(target=calcula_soma)
    t2 = threading.Thread(target=calcula_soma)

    start_time = time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('estou neste ponto!')

    print('-----------------------------------------------------------')
    print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
    print('-----------------------------------------------------------')

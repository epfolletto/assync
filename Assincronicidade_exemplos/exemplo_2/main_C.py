import time
import multiprocessing


def calcula_soma():
    print('Iniciando a função...')
    soma = 0
    for _ in range(300_000_000):
        soma = soma + 1
    print('Cálculo finalizado.')


if __name__ == '__main__':
    cod1 = multiprocessing.Process(target=calcula_soma)
    cod2 = multiprocessing.Process(target=calcula_soma)

    start_time = time.time()

    cod1.start()
    cod2.start()

    cod1.join()
    cod2.join()

    print('estou neste ponto!')

    print('-----------------------------------------------------------')
    print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
    print('-----------------------------------------------------------')

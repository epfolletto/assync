import time
import concurrent.futures

start_time = time.time()


def calcula_soma(numero):
    print('Iniciando a função...')
    soma = 0
    for _ in range(numero):
        soma = soma + 1
    return f'Cálculo finalizado - num: {numero}.'


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nums = [300_000_000, 300_000_000]
        cods = executor.map(calcula_soma, nums)

        for cod in cods:
            print(cod)

    print('estou neste ponto!')

    print('-----------------------------------------------------------')
    print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
    print('-----------------------------------------------------------')

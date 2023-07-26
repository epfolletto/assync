import time


def calcula_soma():
    print('Iniciando a função...')
    soma = 0
    for _ in range(300_000_000):
        soma = soma + 1
    print('Cálculo finalizado.')


start_time = time.time()

calcula_soma()
calcula_soma()

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

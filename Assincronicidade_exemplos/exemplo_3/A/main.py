from tasks import classifica
import time

start_time = time.time()

lista_letras = ['a', 'b', 'c', 'd']

lista_frutas = []
for letra in lista_letras:
    fruta = classifica(letra)
    lista_frutas.append(fruta)

print('lista_frutas:', lista_frutas)

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

from tasks import classifica
import time

start_time = time.time()

lista_letras = ['a', 'b', 'c', 'd']

lista_frutas = []
for letra in lista_letras:
    fruta = classifica.delay(letra)
    lista_frutas.append(fruta)

print('lista_frutas:', lista_frutas)

print('estou neste ponto!')

print('-----------------------------------------------------------')
print(f"Tempo de execução 1: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

while True:
    res = all(tarefa.ready() for tarefa in lista_frutas)
    if res == True:
        print('-----------------------------------------------------------')
        print(f"Tempo de execução 2: {time.time() - start_time:.5f} segundos")
        print('-----------------------------------------------------------')
        break

import asyncio
import time


async def tarefa_async(num):
    print('Iniciei a tarefa', num)
    await asyncio.sleep(2)
    print('Finalizei a tarefa', num)


async def main():
    tarefas = []
    for i in range(3):
        tarefa = asyncio.create_task(tarefa_async(i))
        tarefas.append(tarefa)

    await asyncio.gather(*tarefas)


start_time = time.time()

asyncio.run(main())

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

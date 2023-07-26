import asyncio
import time


async def tarefa1():
    print('Iniciei a tarefa 1')
    await asyncio.sleep(2)
    print('Finalizei a tarefa 1')


async def tarefa2():
    print('Iniciei a tarefa 2')
    await asyncio.sleep(2)
    print('Finalizei a tarefa 2')


async def tarefa3():
    print('Iniciei a tarefa 3')
    await asyncio.sleep(2)
    print('Finalizei a tarefa 3')


async def main():
    tar1 = asyncio.create_task(tarefa1())
    tar2 = asyncio.create_task(tarefa2())
    tar3 = asyncio.create_task(tarefa3())

    await tar1
    await tar2
    await tar3


start_time = time.time()

asyncio.run(main())

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

import aiohttp
import asyncio
import time


async def main():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


start_time = time.time()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())


# asyncio.run(main())

print('-----------------------------------------------------------')
print(f"Tempo de execução: {time.time() - start_time:.5f} segundos")
print('-----------------------------------------------------------')

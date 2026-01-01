import asyncio
import aiohttp
import aiofiles


async def greet():
    print("greet called start")
    await asyncio.sleep(10)
    print("greet called end")
    return "Hello, Async World! from greet"


async def greet2():
    greet2 = "hello"
    Session = aiohttp.ClientSession()
    print("greet2 called start")
    url = 'https://api.agify.io/?name=meelad'
    async with Session.get(url) as response:
        data = await response.json()
        print(data)
        greet2 = data
    await Session.close()
    print("greet2 called end")
    return f"Hello, Async World! from greet2 with data: {greet2}"


async def greet3():
    greet3 = "hello"
    read_file = 'poc/sample.txt'
    async with aiofiles.open(read_file, mode='r') as f:
        contents = await f.read()
        print(contents)
        greet3 = contents
    print("greet3 called end")
    return f"Hello, Async World! from greet3 with data: {greet3}"


async def main():
    message = await greet()
    message2, message3 = await asyncio.gather(greet2(), greet3())
    print(message)
    print(message2)
    print(message3)


if __name__ == "__main__":
    asyncio.run(main())
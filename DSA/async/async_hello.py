import asyncio
from util.delay_functions import delay, delay_version2

async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return "Hello World"


async def main() -> None:
    message = await hello_world_message()
    print(message)

    test = await delay(3)
    test = await delay_version2(2, "john")
    print(test)

    print("ABC")
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
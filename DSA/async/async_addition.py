import asyncio



async def add_one(number: int) -> int:
    return number +1

async def main() -> None:
    starting_number = 10

    # in here one is paused and wait for the results
    one = await add_one(starting_number)

    print(one)
    
    # in here two is paused and wait for the results
    two = await add_one(one)
    print(two)

if __name__=='__main__':
    asyncio.run(main())
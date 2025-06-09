import asyncio
import time
from util.delay_functions import delay, delay_version2


# on this example, you would see that 
# the asyncio.create_task() will create 
# the task almost immediately and schedule it to run 
# as soon as possible. In this case, three
# tasks is being scheduled and pending

# as soon as the await function is called
# any tasks that are pending will run await
# and an iteration of the event loop

async def more_sleep(duration: int):
    print(f"sleeping {duration} seconds")
    await asyncio.sleep(duration)
    print(f"slept for {duration}")


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("im running other code whilst waiting")

async def main():
    # in here the asyncio tasks is executed
    sleep_for_three = asyncio.create_task(more_sleep(3))
    sleep_2 = asyncio.create_task(more_sleep(3))
    sleep_more = asyncio.create_task(more_sleep(3))


    await hello_every_second()

    await sleep_for_three
    await sleep_2
    await sleep_more

    print("im here")

if __name__ == "__main__":
    asyncio.run(
        main()
        )
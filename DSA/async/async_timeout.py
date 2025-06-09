import asyncio
from util.delay_functions import delay


# asyncio.wait_for is used to set a timeout
# if the timeout triggers, then
# it will raise an exception

async def main():
    delay_task  = asyncio.create_task(delay(3))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("received timeout")
        print(f"was the task cancelled {delay_task.cancelled()} " )


if __name__ == "__main__":
    asyncio.run(main())
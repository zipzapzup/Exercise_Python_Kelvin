import asyncio

async def delay(delay_seconds: int ) -> int:
    print(f"sleeping for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds}")
    return delay_seconds




async def delay_version2( delay_seconds: int, name: str) -> int:
    print( f"{name} is put into sleep for: {delay_seconds} seconds")

    await asyncio.sleep(delay_seconds)

    print(f"{name} is awake and has been asleep for {delay_seconds} second(s)")
    return delay_seconds

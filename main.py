import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(3))
    try:
        result = await asyncio.wait_for(delay_task, timeout=4)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Got a timeout!')
    finally:
        print(f'Was the task cancelled? {delay_task.cancelled()}')

asyncio.run(main())
import asyncio
import time

# Local imports

from utils import print_error

async def main():

    try:
        print()
        time.sleep(1)

    except Exception as error:
        print_error(error)

    finally:
        print()
        print('finally')

asyncio.run(main())
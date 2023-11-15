import asyncio
from urllib.parse import urlencode

import aiohttp

from tests.test_data import test_requests


async def run_script():
    """Run test reuests."""
    async with aiohttp.ClientSession() as session:
        for request in test_requests:
            encoded_params = urlencode(request)
            response = await session.post(
                url='http://127.0.0.1:8000/get_form',
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                data=encoded_params,
            )
            print(f'Входные данные: {encoded_params}')
            print(f'Ответ. Статус код: {response.status}')
            print(f'Ответ. Данные: {await response.json()}')
            print()


if __name__ == '__main__':
    asyncio.run(run_script())

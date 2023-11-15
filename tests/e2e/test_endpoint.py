import aiohttp
from urllib.parse import urlencode

import pytest

from tests.test_data import parametrized_values


@pytest.mark.parametrize(
        'test_request, expected_result',
        parametrized_values,
)
async def test_get_form(test_request, expected_result):
    """Check normal work of `get_form` endpoint."""
    async with aiohttp.ClientSession() as session:

        response = await session.post(
            url='http://127.0.0.1:8000/get_form',
            data=urlencode(test_request),
        )
        assert await response.json() == expected_result['response']
        assert response.status == expected_result['status']

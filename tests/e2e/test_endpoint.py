from urllib.parse import urlencode

import pytest
from fastapi.testclient import TestClient

from form_app.main import app
from tests.test_data import parametrized_values


@pytest.mark.parametrize(
        'test_request, expected_result',
        parametrized_values,
)
async def test_get_form(test_request, expected_result):
    """Check normal work of `get_form` endpoint."""
    with TestClient(app) as client:
        response = client.post(
            url='/get_form',
            data=urlencode(test_request),
        )
        assert response.json() == expected_result['response']
        assert response.status_code == expected_result['status']

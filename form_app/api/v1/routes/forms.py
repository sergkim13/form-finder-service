from fastapi import APIRouter, Depends, Request
from starlette.status import HTTP_200_OK

from form_app.api.v1.dependencies import get_form_service
from form_app.services.forms import FormService
from form_app.services.parser import get_body_params

router = APIRouter(
    prefix='',
    tags=['Forms'],
)


@router.post(
    path='/get_form',
    status_code=HTTP_200_OK,
    summary='Get form',
)
async def get_form(
    request: Request,
    form_service: FormService = Depends(get_form_service),
) -> str | dict:
    """
    Find a form compatible with requests's felds and return it's name.
    If form not found return a dictionary with request'fields names and types.
    """
    body = await request.body()
    body_params = get_body_params(body)
    result = await form_service.find_form_template(body_params)
    return result

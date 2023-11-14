from fastapi import APIRouter, Depends, Request
from starlette.status import HTTP_200_OK

from form_app.services.forms import FormService
from form_app.api.v1.dependencies import get_form_service


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
):
    query_param_dict = dict(request.query_params)
    result = await form_service.find_form(query_param_dict)
    return result
from fastapi import APIRouter
from starlette.status import HTTP_200_OK


router = APIRouter(
    prefix='',
    tags=['Forms'],
)


@router.post(
    path='/get_form',
    status_code=HTTP_200_OK,
    summary='Get form',
)
async def get_form():
    return 'HI'

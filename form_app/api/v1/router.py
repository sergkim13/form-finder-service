from fastapi import APIRouter

from form_app.api.v1.routes.forms import router


api_router = APIRouter(
    prefix='/api/v1',
)

api_router.include_router(router)

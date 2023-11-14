from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from form_app.api.v1.router import api_router
from form_app.core.config import settings
from form_app.middleware.query import QueryValdationMiddleware
from form_app.services.utils import populate_db_with_forms


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Drop database and populate with for on app start."""
    await populate_db_with_forms()
    yield


app = FastAPI(
    title='Form app API',
    description='Form app API, powered by FastAPI',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
    lifespan=lifespan,
)
app.include_router(api_router)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.add_middleware(QueryValdationMiddleware)

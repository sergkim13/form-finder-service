from fastapi import FastAPI

from form_app.api.v1.router import api_router

app = FastAPI(
    title='Form app API',
    description='Form app API, powered by FastAPI',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
)
app.include_router(api_router)

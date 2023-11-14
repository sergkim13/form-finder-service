from typing import Callable

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from form_app.services.parser import get_body_params
from form_app.validation.field_validators import validate_date, validate_phone, validate_email


class BodyValdationMiddleware(BaseHTTPMiddleware):
    """Custom middleware for validation body parameters."""

    async def set_body(self, request: Request):
        """Custom `set_body` method to get request body in middleware."""
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next: Callable):
        """Custom `disptatch` method for validate body parameters."""
        await self.set_body(request)
        VALIDATION_MAP = {
            'date': validate_date,
            'phone': validate_phone,
            'email': validate_email,
        }
        errors = []
        body = await request.body()
        body_params = get_body_params(body)

        for field_name, field_value in body_params.items():
            field_type = field_name.split('_')[-1]
            if field_type in VALIDATION_MAP:
                try:
                    validation_func = VALIDATION_MAP[field_type]
                    validation_func(field_value)
                except ValueError as exc:
                    errors.append(str(exc))

        if errors:
            return JSONResponse(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                content=errors,
            )
        return await call_next(request)

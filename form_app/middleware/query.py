import re
from datetime import datetime
from typing import Callable

from email_validator import validate_email, EmailNotValidError
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from form_app.validation.field_validators import validate_date, validate_phone, validate_email


class QueryValdationMiddleware(BaseHTTPMiddleware):
    """Custom middleware for validation query parameters."""

    async def dispatch(self, request: Request, call_next: Callable):
        """Custom `disptatch` method for validate query parameters."""
        VALIDATION_MAP = {
            'date': validate_date,
            'phone': validate_phone,
            'email': validate_email,
        }
        errors = []
        query_params = dict(request.query_params)

        for field_name, field_value in query_params.items():
            field_type = field_name.split('_')[-1]
            if field_type in VALIDATION_MAP:
                try:
                    validation_func: Callable = VALIDATION_MAP[field_type]
                    validation_func(field_value)
                except ValueError as exc:
                    errors.append(str(exc))

        if errors:
            return JSONResponse(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                content=errors,
            )
        return await call_next(request)

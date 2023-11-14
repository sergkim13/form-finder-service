import re
from datetime import datetime

from email_validator import validate_email as validate, EmailNotValidError


def validate_date(value: str) -> bool:
    """Validate date value."""
    format1 = '%Y-%m-%d'
    format2 = '%d.%m.%Y'
    errors = []
    try:
        datetime.strptime(value, format1)
    except ValueError as exc1:
        errors.append(str(exc1))
        try:
            datetime.strptime(value, format2)
        except ValueError as exc2:
            errors.append(str(exc2))
    finally:
        if len(errors) == 2:
            raise ValueError(f"date data '{value}' does not match format %Y-%m-%d' or '%d.%m.%Y'")

    return True


def validate_phone(value: str) -> bool:
    """Validate phone value."""
    phone_format = r'^\+7\d{10}$'

    if not re.match(phone_format, value):
        raise ValueError(f"phone data {value} does not match format '+7 xxx xx xx'")

    return True


def validate_email(value: str) -> bool:
    """Validate email value."""
    try:
        validate(value)
    except EmailNotValidError as exc:
        raise ValueError(str(exc))

    return True

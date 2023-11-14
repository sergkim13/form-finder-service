from form_app.repository.abstract import AbstractRepository
from form_app.validation.field_validators import validate_date, validate_email, validate_phone


class FormService:
    """Service class which provides forms handling operations."""

    def __init__(self, form_repository: AbstractRepository) -> None:
        """Inits `FormService` instance."""
        self.form_repository = form_repository

    async def find_form_template(self, parameters: dict) -> dict:
        """
        Finds form in database and returns it's name or dict with field names and types
        if compatible form not found.
        """
        form_to_find = self._build_form_to_find(parameters)
        form = await self.form_repository.get(form_to_find)

        if not form:
            return form_to_find

        return form['name']

    def _build_form_to_find(self, form_dict: dict) -> dict:
        """Builds a dict with field names and types."""
        TYPES = ['date', 'phone', 'email']
        form_to_find = {}

        for field_name, field_value in form_dict.items():
            field_type = field_name.split('_')[-1]
            if field_type in TYPES:
                form_to_find[field_name] = field_type
            else:
                form_to_find[field_name] = self._define_field_type(field_value)

        return form_to_find

    def _define_field_type(self, field_value: str) -> str:
        """Defines a field type: date, phone, email or text."""
        field_type = 'text'
        try:
            validate_date(field_value)
            field_type = 'date'
        except ValueError:
            pass
        try:
            validate_phone(field_value)
            field_type = 'phone'
        except ValueError:
            pass
        try:
            validate_email(field_value)
            field_type = 'email'
        except ValueError:
            pass

        return field_type

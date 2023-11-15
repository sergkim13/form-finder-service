from form_app.repository.abstract import AbstractRepository
from form_app.validation.field_validators import validate_date, validate_email, validate_phone


class FormService:
    """Service class which provides forms handling operations."""

    def __init__(self, form_repository: AbstractRepository) -> None:
        """Init `FormService` instance."""
        self.form_repository = form_repository

    async def find_form_template(self, parameters: dict) -> dict:
        """
        Find form in database and returns it's name or dict with field names and types
        if compatible form not found.
        """
        form_to_find = self._build_form_to_find(parameters)
        forms_list = await self.form_repository.read_all()
        serialized_forms_list = self._get_serialized_form_list(forms_list)
        compatible_form = self._find_compatible_form(serialized_forms_list, form_to_find)

        if not compatible_form:
            return form_to_find

        return compatible_form['form_name']

    def _get_serialized_form_list(self, forms_list: list[dict]) -> list[dict]:
        """Serialize forms list to list of dict with sets of forms fields."""
        forms_list = [self._remove_id_field(form) for form in forms_list]

        return [
            {
                'form_name': form['name'],
                'form_fields': {
                    (key, value) for key, value in form.items() if key != 'name'
                    }
            } for form in forms_list
        ]

    def _remove_id_field(self, form: dict) -> dict:
        """Remove _id field from form dict."""
        return {key: value for key, value in form.items() if key != '_id'}

    def _find_compatible_form(self, serialized_forms_list: list[dict], form_to_find: dict):
        """Find compatible form or return None."""
        form_to_find_set = {item for item in form_to_find.items()}
        print(len(form_to_find_set))
        for form in serialized_forms_list:
            if form['form_fields'].issubset(form_to_find_set):
                return form

        return None

    def _build_form_to_find(self, form_dict: dict) -> dict:
        """Build a dict with field names and types."""
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
        """Define a field type: date, phone, email or text."""
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

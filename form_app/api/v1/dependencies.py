from form_app.services.forms import FormService
from form_app.repository.mongo_motor import MongoMotorDBRepository
from form_app.core.config import settings


def get_form_service():
    """
    Returns a FormSevice instance with MongoMotorDBRepository as form repository.
    Used for dependency injection.
    """
    form_repository = MongoMotorDBRepository(db_url=settings.db_url)
    return FormService(form_repository)

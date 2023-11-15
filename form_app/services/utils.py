from form_app.core.config import settings
from form_app.data.forms_examples import forms
from form_app.repository.mongo_motor import MongoMotorDBRepository


async def populate_db_with_forms():
    """Drop database and creates forms."""

    mongo_repo = MongoMotorDBRepository(db_url=settings.db_url)
    await mongo_repo.client.drop_database(settings.DB_NAME)
    await mongo_repo.create(forms)

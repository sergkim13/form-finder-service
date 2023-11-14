from form_app.core.config import settings
from form_app.repository.mongo_motor import MongoMotorDBRepository


async def populate_db_with_forms():
    """Drop database and creates forms."""
    forms = [
        {
            'name': 'OrderForm',
            'order_date': 'date',
            'customer_phone': 'phone',
            'customer_email': 'email',
            'order_item': 'text',
        },
        {
            'name': 'DeliveryForm',
            'deliver_date': 'date',
            'customer_phone': 'phone',
            'address': 'text',
        },
        {
            'name': 'UserForm',
            'birth_date': 'date',
            'user_phone': 'phone',
            'user_email': 'email',
        },
        {
            'name': 'ResumeForm',
            'created_at_date': 'date',
            'candidate_email': 'email',
            'job_title': 'text',
        },
        {
            'name': 'VacancyForm',
            'created_at_date': 'date',
            'hr_phone': 'phone',
            'hr_email': 'email',
            'job_description': 'text',
        },
    ]
    mongo_repo = MongoMotorDBRepository(db_url=settings.db_url)
    await mongo_repo.client.drop_database(settings.DB_NAME)
    await mongo_repo.create(forms)

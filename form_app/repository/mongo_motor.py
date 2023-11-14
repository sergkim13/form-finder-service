from form_app.repository.abstract import AbstractRepository
from motor.motor_asyncio import AsyncIOMotorClient
from form_app.core.config import settings


class MongoMotorDBRepository(AbstractRepository):
    """Forms repository which implemented on MongoDB wit motor library."""

    def __init__(self, db_url: str) -> None:
        """Inits `MongoMotorDBRepository` instance."""
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client[settings.DB_NAME]

    async def get(self, filter_fields: dict) -> dict | None:
        """Returns a form with given fields or None if form not found."""
        async with await self.client.start_session() as session:
            cursor = self.db.forms.find_one(filter_fields, session=session)
            form = await cursor

        if not form:
            return None

        return form

    async def create(self, documents: list[dict]):
        """Creates forms."""
        async with await self.client.start_session() as session:
            await self.db.forms.insert_many(documents, session=session)

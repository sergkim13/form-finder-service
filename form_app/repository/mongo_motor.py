from form_app.repository.abstract import AbstractRepository
from motor.motor_asyncio import AsyncIOMotorClient
from form_app.core.config import settings


class MongoMotorDBRepository(AbstractRepository):
    """Forms repository which implemented on MongoDB wit motor library."""

    def __init__(self, db_url: str) -> None:
        """Init `MongoMotorDBRepository` instance."""
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client[settings.DB_NAME]

    async def read_all(self) -> list | None:
        """Return all forms from database."""
        async with await self.client.start_session() as session:
            cursor = self.db.forms.find(session=session)
            return await cursor.to_list(None)

    async def create(self, documents: list[dict]):
        """Create forms."""
        async with await self.client.start_session() as session:
            await self.db.forms.insert_many(documents, session=session)

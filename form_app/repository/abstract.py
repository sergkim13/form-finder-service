from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError

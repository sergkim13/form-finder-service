from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def read_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError

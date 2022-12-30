from unittest import IsolatedAsyncioTestCase, main
from functools import partial

from repositories.service_repository import ServiceRepository
from common.db import MongoClient
from common.promise import Promise
from models.service import Service


class ServiceTests(IsolatedAsyncioTestCase):

    async def test_get_by_id_should_return_none(self):
        MongoClient().connect()
        service_repository = ServiceRepository(Service)
        service: Service | None = await Promise.resolve(
            partial(service_repository.get_by_id, "63ae6eb779b9416155e3c476")
        )
        self.assertIsNone(service)

if __name__ == '__main__':
    main()

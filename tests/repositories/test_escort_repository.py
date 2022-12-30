# from unittest import IsolatedAsyncioTestCase, main
# from functools import partial

# from repositories.escort_repository import EscortRepository
# from common.db import PostgresClient
# from common.promise import Promise
# from models.escort_profile import EscortProfile


# class EscortRepositoryTests(IsolatedAsyncioTestCase):

#     async def test_get_by_id_should_return_none(self):
#         postgres_client: dict = PostgresClient().connect()
#         escort_repository = EscortRepository(postgres_client['escort_db'])
#         profile: EscortProfile | None = await Promise.resolve(
#             partial(escort_repository.get_by_id, "dummy id")
#         )
#         self.assertIsNone(profile)

# if __name__ == '__main__':
#     main()

# from unittest import IsolatedAsyncioTestCase, main
# from functools import partial

# from repositories.customer_repository import CustomerRepository
# from common.db import PostgresClient
# from common.promise import Promise
# from models.customer_profile import CustomerProfile


# class CustomerRepositoryTests(IsolatedAsyncioTestCase):

#     async def test_get_by_id_should_return_none(self):
#         postgres_client: dict = PostgresClient().connect()
#         customer_repository =  CustomerRepository(postgres_client['customer_db'])
#         profile: CustomerProfile | None = await Promise.resolve(
#             partial(customer_repository.get_by_id, "dummy id")
#         )
#         self.assertIsNone(profile)

# if __name__ == '__main__':
#     main()

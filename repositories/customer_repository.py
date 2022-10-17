from __future__ import annotations

from psycopg2._psycopg import connection, cursor

from models.customer_profile import CustomerProfile


class CustomerRepository:

    def __init__(self, postgres_client: connection):
        self.__postgres_client = postgres_client

    def get_by_id(self, customer_id: str) -> CustomerProfile | None:
        conn: cursor = self.__postgres_client.cursor()
        conn.execute(f"SELECT customer_id, first_name, last_name FROM profile WHERE customer_id = '{customer_id}';")
        rows: list = conn.fetchall()

        try:
            customer_profile: CustomerProfile = CustomerProfile()
            customer_profile.customer_id = rows[0][0]
            customer_profile.first_name = rows[0][1]
            customer_profile.last_name = rows[0][2]

            return customer_profile
        except Exception as e:
            print('Error getting escort profile: ', e)
            return None

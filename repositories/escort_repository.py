from __future__ import annotations

from psycopg2._psycopg import connection, cursor

from models.escort_profile import EscortProfile


class EscortRepository:

    def __init__(self, postgres_client: connection):
        self.__postgres_client = postgres_client

    def get_by_id(self, escort_id: str) -> EscortProfile | None:
        conn: cursor = self.__postgres_client.cursor()
        conn.execute(f"SELECT escort_id, first_name, last_name FROM profile WHERE escort_id = '{escort_id}';")
        rows: list = conn.fetchall()

        try:
            escort_profile = EscortProfile()
            escort_profile.escort_id = rows[0][0]
            escort_profile.first_name = rows[0][1]
            escort_profile.last_name = rows[0][2]

            return escort_profile
        except Exception as e:
            print('Error getting escort profile: ', e)
            return None

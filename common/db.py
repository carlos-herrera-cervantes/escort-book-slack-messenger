import psycopg2
import mongoengine

from common.singleton import SingletonMeta
from settings.postgres import PostgresClient as PostgresSettings, PostgresDB
from settings.mongo import MongoClient as MongoSettings


class MongoClient(metaclass=SingletonMeta):

    def __init__(self):
        self.__db = MongoSettings.MONGO_URI.value

    def connect(self) -> None:
        print('Successful connected to MongoDB')
        mongoengine.connect(host=self.__db)


class PostgresClient(metaclass=SingletonMeta):

    def __init__(self):
        self.__escort_db = (
            f'dbname={PostgresDB.ESCORT.value} ' +
            f'user={PostgresSettings.USER_DB.value} ' +
            f'password={PostgresSettings.PASSWORD_DB.value} ' +
            f'host={PostgresSettings.ESCORT_DB_HOST.value} ' +
            f'port={PostgresSettings.PORT_DB.value}'
        )

        self.__customer_db = (
            f'dbname={PostgresDB.CUSTOMER.value} ' +
            f'user={PostgresSettings.USER_DB.value} ' +
            f'password={PostgresSettings.PASSWORD_DB.value} ' +
            f'host={PostgresSettings.CUSTOMER_DB_HOST.value} ' +
            f'port={PostgresSettings.PORT_DB.value}'
        )

    def connect(self) -> dict:
        connections: dict = {
            'escort_db': psycopg2.connect(self.__escort_db),
            'customer_db': psycopg2.connect(self.__customer_db)
        }
        print('Successful connected to Postgres')
        return connections

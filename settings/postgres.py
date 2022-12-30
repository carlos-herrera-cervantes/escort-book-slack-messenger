import os
from enum import Enum


class PostgresClient(Enum):
    USER_DB = os.getenv('USER_DB')
    PASSWORD_DB = os.getenv('PASSWORD_DB')
    ESCORT_DB_HOST = os.getenv('ESCORT_DB_HOST')
    CUSTOMER_DB_HOST = os.getenv('CUSTOMER_DB_HOST')
    PORT_DB = int(os.getenv('PORT_DB'))


class PostgresDB(Enum):
    ESCORT = os.getenv('ESCORT_DB')
    CUSTOMER = os.getenv('CUSTOMER_DB')

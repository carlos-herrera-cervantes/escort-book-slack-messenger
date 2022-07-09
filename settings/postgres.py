import os
from enum import Enum


class PostgresClient(Enum):
    USER_DB = os.getenv('USER_DB')
    PASSWORD_DB = os.getenv('PASSWORD_DB')
    HOST_DB = os.getenv('HOST_DB')
    PORT_DB = int(os.getenv('PORT_DB'))


class PostgresDB(Enum):
    ESCORT = os.getenv('ESCORT_DB')
    CUSTOMER = os.getenv('CUSTOMER_DB')

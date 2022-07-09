import os
from enum import Enum


class MongoClient(Enum):
    DEFAULT_DB = os.getenv('DEFAULT_DB')

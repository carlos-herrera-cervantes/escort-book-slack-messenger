from unicodedata import decimal
from datetime import datetime

from mongoengine import *


class Service(Document):
    customerId: str = ObjectIdField()
    escortId: str = ObjectIdField()
    price: decimal = DecimalField()
    businessCommission: decimal = DecimalField()
    status: str = StringField()
    timeQuantity: int = IntField()
    timeMeasurementUnit: str = StringField()
    details: list = ListField()
    paymentDetails: list = ListField()
    createdAt: datetime = DateTimeField()
    updatedAt: datetime = DateTimeField()
    meta = {'collection': 'services'}

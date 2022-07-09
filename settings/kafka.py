import os
from enum import Enum


class KafkaClient(Enum):
    BOOTSTRAP_SERVERS = os.getenv('KAFKA_HOSTS')
    GROUP_ID = os.getenv('CONSUMER_GROUP_ID')


class KafkaTopics(Enum):
    SERVICE_CREATED = 'service-created'
    SERVICE_STARTED = 'service-started'
    SERVICE_PAID = 'operations-statistics'

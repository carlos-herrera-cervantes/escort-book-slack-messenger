import http.client

from processors.interfaces.service_status_strategy import Strategy
from processors.strategies.service_status import ServiceStatus
from settings.kafka import KafkaTopics
from repositories.service_repository import ServiceRepository
from repositories.escort_repository import EscortRepository
from repositories.customer_repository import CustomerRepository
from services.slack_service import SlackService
from models.service import Service
from common.db import PostgresClient, MongoClient


class StrategyManager:

    def __init__(self, topic: str):
        MongoClient().connect()

        postgres_client: dict = PostgresClient().connect()
        service_status: ServiceStatus = ServiceStatus(
            ServiceRepository(Service),
            EscortRepository(postgres_client['escort_db']),
            CustomerRepository(postgres_client['customer_db']),
            SlackService(http.client),
        )

        self.__topic = topic
        self.__strategies: dict = {
            KafkaTopics.SERVICE_CREATED.value: service_status,
            KafkaTopics.SERVICE_STARTED.value: service_status,
            KafkaTopics.SERVICE_PAID.value: service_status,
        }

    async def run_task(self, message: dict) -> None:
        strategy: Strategy = self.__strategies.get(self.__topic)

        if not strategy:
            return

        await strategy.process_message(message)


def initialize_manager(topic: str) -> StrategyManager:
    return StrategyManager(topic)

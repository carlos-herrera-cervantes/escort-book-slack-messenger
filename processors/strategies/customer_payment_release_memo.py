from functools import partial

from processors.interfaces.service_status_strategy import Strategy
from repositories.service_repository import ServiceRepository
from repositories.customer_repository import CustomerRepository
from services.slack_service import SlackService
from models.service import Service
from models.customer_profile import CustomerProfile
from settings.slack import SlackClient, MessageTemplates
from common.promise import Promise


class CustomerPaymentReleaseMemo(Strategy):

    def __init__(
        self,
        service_repository: ServiceRepository,
        customer_repository: CustomerRepository,
        slack_service: SlackService,
    ):
        self.__service_repository = service_repository
        self.__customer_repository = customer_repository
        self.__slack_service = slack_service

    async def process_message(self, message: dict) -> None:
        service: Service = await Promise.resolve(
            partial(self.__service_repository.get_by_id, message['serviceId'])
        )

        if not service:
            print('Service does not exist')
            return

        customer: CustomerProfile = await Promise.resolve(
            partial(self.__customer_repository.get_by_id, service.customerId)
        )

        template: dict = MessageTemplates.CUSTOMER_RELEASE_PAYMENT.value
        text: str = template.get('text', '')
        slack_message: str = (
            text
            .replace('{{service_id}}', message['serviceId'])
            .replace('{{customer_name}}', f'{customer.first_name} {customer.last_name}')
        )
        request_body: dict = {'text': slack_message}
        
        (await self.__slack_service
            .send_message(SlackClient.HOST.value, SlackClient.PATH.value, request_body))

from functools import partial

from processors.interfaces.service_status_strategy import Strategy
from repositories.service_repository import ServiceRepository
from repositories.escort_repository import EscortRepository
from services.slack_service import SlackService
from models.service import Service
from models.escort_profile import EscortProfile
from settings.slack import SlackClient, MessageTemplates
from common.promise import Promise


class EscortPaymentReleaseMemo(Strategy):

    def __init__(
        self,
        service_repository: ServiceRepository,
        escort_repository: EscortRepository,
        slack_service: SlackService,
    ):
        self.__service_repository = service_repository
        self.__escort_repository = escort_repository
        self.__slack_service = slack_service

    async def process_message(self, message: dict) -> None:
        service: Service = await Promise.resolve(
            partial(self.__service_repository.get_by_id, message['serviceId'])
        )

        if not service:
            print('Service does not exist')
            return

        escort: EscortProfile = await Promise.resolve(
            partial(self.__escort_repository.get_by_id, service.escortId)
        )

        template: dict = MessageTemplates.ESCORT_RELEASE_PAYMENT.value
        text: str = template.get('text', '')
        slack_message: str = (
            text
            .replace('{{service_id}}', message['serviceId'])
            .replace('{{escort_name}}', f'{escort.first_name} {escort.last_name}')
        )
        request_body: dict = {'text': slack_message}
        
        (await self.__slack_service
            .send_message(SlackClient.HOST.value, SlackClient.PATH.value, request_body))

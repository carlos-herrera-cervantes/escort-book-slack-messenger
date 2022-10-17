from unittest.mock import Mock
from unittest import IsolatedAsyncioTestCase, main
from asyncio import AbstractEventLoop, get_event_loop, Future

from processors.strategies.service_status import ServiceStatus
from models.service import Service
from models.customer_profile import CustomerProfile
from models.escort_profile import EscortProfile

def mock_send_message() -> None:
    return None


class ServiceStatusTests(IsolatedAsyncioTestCase):

    async def test_process_message_should_return_none(self) -> None:
        mock_service_repository: Mock = Mock()
        mock_service_repository.get_by_id.return_value = None

        service_status_strategy: ServiceStatus = ServiceStatus(
            mock_service_repository,
            None,
            None,
            None
        )
        message: dict = {'serviceId': '634c5225d92e197cb5cff750'}

        got = await service_status_strategy.process_message(message)

        self.assertIsNone(got)
        self.assertTrue(mock_service_repository.get_by_id.called)

    async def test_process_message_should_send_message(self) -> None:
        mock_service_repository: Mock = Mock()
        mock_service_repository.get_by_id.return_value = Service(**{
            'escortId': '634c65791c6476e3eecef39e',
            'customerId': '634c65828693c4ffe844c897',
            'status': 'started',
        })

        mock_escort_repository: Mock = Mock()
        escort: EscortProfile = EscortProfile()
        escort.first_name = 'Ruth'
        escort.last_name = 'Villa'
        mock_escort_repository.get_by_id.return_value = escort

        mock_customer_repository: Mock = Mock()
        customer: CustomerProfile = CustomerProfile()
        customer.first_name = 'Carlos'
        customer.last_name = 'Herrera'
        mock_customer_repository.get_by_id.return_value = customer

        mock_slack_service = Mock()
        loop: AbstractEventLoop = get_event_loop()
        future: Future = loop.run_in_executor(None, mock_send_message)
        mock_slack_service.send_message.return_value = future

        service_status_strategy: ServiceStatus = ServiceStatus(
            mock_service_repository,
            mock_escort_repository,
            mock_customer_repository,
            mock_slack_service
        )
        message: dict = {'serviceId': '634c5225d92e197cb5cff750'}

        await service_status_strategy.process_message(message)

        self.assertTrue(mock_service_repository.get_by_id.called)
        self.assertTrue(mock_escort_repository.get_by_id.called)
        self.assertTrue(mock_customer_repository.get_by_id.called)
        self.assertTrue(mock_slack_service.send_message.called)

if __name__ == '__main__':
    main()

from unittest.mock import Mock
from unittest import IsolatedAsyncioTestCase, main
from asyncio import AbstractEventLoop, get_event_loop, Future

from processors.strategies.customer_payment_release_memo import CustomerPaymentReleaseMemo
from models.service import Service
from models.customer_profile import CustomerProfile

def mock_send_message() -> None:
    return None


class CustomerPaymentReleaseMemoTests(IsolatedAsyncioTestCase):

    async def test_process_message_should_return_none(self) -> None:
        mock_service_repository = Mock()
        mock_service_repository.get_by_id.return_value = None

        customer_payment_release_strategy: CustomerPaymentReleaseMemo = CustomerPaymentReleaseMemo(
            mock_service_repository,
            None,
            None
        )
        message: dict = {'serviceId': '634c5225d92e197cb5cff750'}

        got = await customer_payment_release_strategy.process_message(message)

        self.assertIsNone(got)
        self.assertTrue(mock_service_repository.get_by_id.called)

    async def test_process_message_should_send_message(self) -> None:
        mock_service_repository = Mock()
        mock_service_repository.get_by_id.return_value = Service(**{
            'customerId': '634c596332d3b0bcc3063384',
        })
        
        mock_customer_repository = Mock()
        customer: CustomerProfile = CustomerProfile()
        customer.first_name = 'Carlos'
        customer.last_name = 'Herrera'
        mock_customer_repository.get_by_id.return_value = customer
        
        mock_slack_service = Mock()
        loop: AbstractEventLoop = get_event_loop()
        future: Future = loop.run_in_executor(None, mock_send_message)
        mock_slack_service.send_message.return_value = future

        customer_payment_release_strategy: CustomerPaymentReleaseMemo = CustomerPaymentReleaseMemo(
            mock_service_repository,
            mock_customer_repository,
            mock_slack_service
        )
        message: dict = {'serviceId': '634c5225d92e197cb5cff750'}

        await customer_payment_release_strategy.process_message(message)

        self.assertTrue(mock_service_repository.get_by_id.called)
        self.assertTrue(mock_customer_repository.get_by_id.called)
        self.assertTrue(mock_slack_service.send_message.called)

if __name__ == '__main__':
    main()

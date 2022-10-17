from unittest.mock import Mock
from unittest import IsolatedAsyncioTestCase, main
from asyncio import AbstractEventLoop, get_event_loop, Future

from processors.strategies.escort_release_payment_memo import EscortPaymentReleaseMemo
from models.service import Service
from models.escort_profile import EscortProfile

def mock_send_message() -> None:
    return None


class EscortReleasePaymentMemoTests(IsolatedAsyncioTestCase):

    async def test_process_message_should_return_none(self) -> None:
        mock_service_repository: Mock = Mock()
        mock_service_repository.get_by_id.return_value = None

        escort_payment_release_strategy: EscortPaymentReleaseMemo = EscortPaymentReleaseMemo(
            mock_service_repository,
            None,
            None
        )
        message: dict = {'serviceId': '634c5225d92e197cb5cff750'}

        got = await escort_payment_release_strategy.process_message(message)

        self.assertIsNone(got)
        self.assertTrue(mock_service_repository.get_by_id.called)

    async def test_process_message_should_send_message(self) -> None:
        mock_service_repository: Mock = Mock()
        mock_service_repository.get_by_id.return_value = Service(**{
            'escortId': '634c596332d3b0bcc3063384'
        })

        mock_escort_repository: Mock = Mock()
        escort: EscortProfile = EscortProfile()
        escort.first_name = 'Ruth'
        escort.last_name = 'Villa'
        mock_escort_repository.get_by_id.return_value = escort

        mock_slack_service = Mock()
        loop: AbstractEventLoop = get_event_loop()
        future: Future = loop.run_in_executor(None, mock_send_message)
        mock_slack_service.send_message.return_value = future

        escort_payment_release_strategy: EscortPaymentReleaseMemo = EscortPaymentReleaseMemo(
            mock_service_repository,
            mock_escort_repository,
            mock_slack_service
        )
        message: dict = {'serviceId': '634c5225d92e197cb5cff750'}

        await escort_payment_release_strategy.process_message(message)

        self.assertTrue(mock_service_repository.get_by_id.called)
        self.assertTrue(mock_escort_repository.get_by_id.called)
        self.assertTrue(mock_slack_service.send_message.called)

if __name__ == '__main__':
    main()

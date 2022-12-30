from unittest.mock import Mock
from unittest import IsolatedAsyncioTestCase, main

from services.slack_service import SlackService


class SlackServiceTests(IsolatedAsyncioTestCase):

    async def test_send_message(self):
        mock_http_client = Mock()
        mock_conn = Mock()

        mock_http_client.HTTPSConnection.return_value = mock_conn
        mock_conn.request.return_value = None

        mock_http_response = Mock()
        mock_http_response.status = 200
        mock_conn.getresponse.return_value = mock_http_response

        slack_service = SlackService(mock_http_client)
        host: str = 'http://localhost'
        path: str = '/dummy-path'
        request_body: dict = {'message': 'dummy message'}
        await slack_service.send_message(host, path, request_body)

        mock_http_client.HTTPSConnection.assert_called_once()
        mock_conn.request.assert_called_once()
        mock_conn.getresponse.asser_called_once()

if __name__ == '__main__':
    main()

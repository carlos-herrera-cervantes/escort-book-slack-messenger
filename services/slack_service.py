import http.client
import asyncio
import json


class SlackService:

    def __init__(self, http_client: http.client):
        self.__http_client = http_client

    async def send_message(self, host: str, path: str, request_body: dict) -> None:
        conn = self.__http_client.HTTPSConnection(host)

        headers: dict = {'Content-Type': 'application/json'}
        body: str = json.dumps(request_body)

        conn.request('POST', path, body, headers)

        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, conn.getresponse)

        response = await future

        print(f'Message send to slack with code: {response.status}')
        print(f'With content: {request_body}')

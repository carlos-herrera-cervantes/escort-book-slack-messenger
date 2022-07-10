import os
from enum import Enum


class SlackClient(Enum):
    HOST = os.getenv('SLACK_HOST')
    PATH = os.getenv('SLACK_PATH')


class MessageTemplates(Enum):
    SERVICE_STATUS = (
        ':ok_alert: The service *{{service_id}}* was change to status *{{status_name}}*. :ok_alert: \n' +
        'Escort: *{{escort_name}}*\nCustomer: *{{customer_name}}*'
    )

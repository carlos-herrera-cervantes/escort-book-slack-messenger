import os
from enum import Enum


class SlackClient(Enum):
    HOST = os.getenv('SLACK_HOST')
    PATH = os.getenv('SLACK_PATH')


class MessageTemplates(Enum):
    SERVICE_STATUS = {
        'text': (
            '✅ The service *{{service_id}}* was change to status *{{status_name}}*. ✅ \n' +
            'Escort: *{{escort_name}}* \nCustomer: *{{customer_name}}*'
        )
    }
    CUSTOMER_RELEASE_PAYMENT = {
        'text': (
            'Service ID: *{{service_id}}* 👩‍🎤 \nCustomer: *{{customer_name}}* 🙋 \n' +
            'Customer was notified that the payment will be released in 10 minutes. 📞 🧭'
        )
    }
    ESCORT_RELEASE_PAYMENT = {
        'text': (
            'Service ID: *{{service_id}}* 🧑‍🎤 \nEscort: *{{escort_name}}* 🙋🏻‍♀️ \n' +
            'The escort was notified that the payment has been released. 💰 💵'
        )
    }

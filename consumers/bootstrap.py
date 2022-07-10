from json import loads

from confluent_kafka import Consumer

from settings.kafka import KafkaClient, KafkaTopics
from processors.strategy_manager import initialize_manager


async def listen() -> None:
    config: dict = {
        'bootstrap.servers': KafkaClient.BOOTSTRAP_SERVERS.value,
        'group.id': KafkaClient.GROUP_ID.value,
        'enable.auto.commit': True,
        'auto.offset.reset': 'earliest',
    }

    consumer = Consumer(config)
    consumer.subscribe([
        KafkaTopics.SERVICE_CREATED.value,
        KafkaTopics.SERVICE_STARTED.value,
        KafkaTopics.SERVICE_PAID.value,
    ])

    try:
        while True:
            message = consumer.poll(1.0)

            if message is None:
                continue
            elif message.error():
                print(f'Error receiving the message {message.error()}')
                continue

            parsed_message: dict = loads(message.value().decode('utf-8'))
            await initialize_manager(message.topic()).run_task(parsed_message)
            print(f'Processed message: {parsed_message}')
    except KeyboardInterrupt:
        print('Gracefully stop the consumer')
    finally:
        consumer.close()

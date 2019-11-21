import asyncio as asio
from aio_pika import connect, IncomingMessage, Message, exchange


class Resiver():

    def __init__(self,  queue='hello', host='192.168.1.8', routingKey='hello', exchange=''):
        self.queue = queue
        self.host = host
        self.connection = None
        self.channel = None
        self.callback_queue = None
        self.exchange = exchange
        self.routingKey = routingKey

class Rabbitmq():

    def __init__(self, server):

        self.server = server
        self.connection = await connect(host=self.server.host,
                                        port=5672,
                                        login='admin',
                                        password='admin',
                                        virtual_host='/'
                                        )
        self.channel = await self.connection.channel()

    def setup(self, payload={}):
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_publish(exchange=self.server.exchange,
                                   routing_key='hello',
                                   body=str(payload)
                                   )
        print("[x] Sent 'Hello!'")
        self.connection.close()


if __name__ == "__main__":
    server = Resiver(queue='hello',
                     host='192.168.1.8',
                     routingKey='hello',
                     exchange='')
    rabbitmq = Rabbitmq(server)
    rabbitmq.setup(payload={"Data:22"})

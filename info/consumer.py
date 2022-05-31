import imp
from channels.generic.websocket import WebsocketConsumer

data = '0;0;deactivate'

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('connected')

    def disconnect(self, code):
        pass

    def receive(self, text_data='', bytes_data=None):
        print(text_data)
        global data
        data = text_data
        self.send(text_data=f'{data[2]}')

class JsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data='', bytes_data=None):
        global data
        self.send(text_data=data)

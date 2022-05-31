from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r'data/$', consumer.Consumer.as_asgi()),
    re_path(r'js/$', consumer.JsConsumer.as_asgi()),
]
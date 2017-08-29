# coding:utf-8
from kombu import Exchange, Queue

CELERY_IMPORTS = ('task',)  # task位于task文件中
MY_BROKER_URL = 'redis://localhost:6379/2'
MY_CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'


config = {
    'CELERY_QUEUES': [
        Queue('A', exchange=Exchange('exchange_add'), routing_key='route_add'),
        Queue('B', exchange=Exchange('exchange_divide'), routing_key='route_divide'),
    ],
    'CELERY_ROUTES': {
        'add': {'queue': 'A'},
        'divide': {'queue': 'B'}
    },

    'CELERY_TIMEZONE': 'Asia/Chongqing',
    'CELERY_ENABLE_UTC' : True,
    'CELERY_ACCEPT_CONTENT': ['pickle', 'json', 'msgpack', 'yaml'],
    'CELERY_TASK_SERIALIZER' : 'json',
    'CELERY_RESULT_SERIALIZER' : 'json',
    'CELERYBEAT_SCHEDULE' : {
        'my_task': {
            'task': 'add', 
            'schedule': 5, 
            'args': (23, 12),
        }
    }
}
from celery import Celery
from celeryconfig import *

app = Celery(
    broker = MY_BROKER_URL,
    backend = MY_CELERY_RESULT_BACKEND,
    include=['task']
    
)

app.config_from_object(config)
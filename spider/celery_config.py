from celery import Celery

app = Celery('celery_config',backend='redis://localhost:6379/0',broker='redis://localhost:6379/0',include=['spider'])

import gevent.monkey
gevent.monkey.patch_socket()

from celery import Celery
import socket
import requests
import gevent

app = Celery('tasks',
             broker='redis://127.0.0.1:6379/3',
             backend='redis://127.0.0.1:6379/3')
@app.task
def spider(url):
    resp = gevent.spawn(requests.get, url)
    tmp = 0
    while True:
        print('wait...', tmp)
        if resp.ready():
            return 'from:' + socket.getfqdn() + '\nres:' + str(resp.value.text)
        gevent.sleep(1)
        tmp += 1

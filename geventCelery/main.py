from tasks import spider
import time
import random

res = spider.delay('http://127.0.0.1:10240/{}'.format(random.randint(1, 999)))
i = 0
while True:
    if res.ready():
        print('res:', res.get())
        break
    else:
        print('wait...', i)
    time.sleep(1)
    i += 1

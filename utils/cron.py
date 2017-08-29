# coding: utf-8
import os
from gevent import monkey

monkey.patch_all(thread=False)

import gevent
from gevent.subprocess import Popen

from config.settings import PROJECT_ROOT

JOBS = [
    ('utils/clean_cache.sh', 60),
    ('sh/celery_kill.sh', 180),
]


class Cron(object):
    def __init__(self, jobs):
        self.jobs = jobs
        self.greenlets = set()

    def run_forever(self, filename, minutes):
        while True:
            gevent.sleep(minutes * 60)
            path = os.path.join(PROJECT_ROOT, filename)
            Popen('bash {0}'.format(path), shell=True)

    def start(self):
        for filename, t in self.jobs:
            self.greenlets.add(gevent.spawn(self.run_forever, filename, t))

        for greenlet in self.greenlets:
            greenlet.join()


def run_cron_jobs():
    return Cron(JOBS).start()


if __name__ == '__main__':
    run_cron_jobs()


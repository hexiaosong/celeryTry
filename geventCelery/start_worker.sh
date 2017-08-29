#!/bin/bash

celery worker -A app --loglevel info -c 100 -P gevent

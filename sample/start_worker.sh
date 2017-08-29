#!/bin/bash

# 启动A,B队列
celery worker -A app -Q A,B -l info
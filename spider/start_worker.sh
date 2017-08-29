#!/bin/bash

celery worker -A celery_config --loglevel=info

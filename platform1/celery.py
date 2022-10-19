# platform1/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "platform1.settings")
app = Celery("platform1")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

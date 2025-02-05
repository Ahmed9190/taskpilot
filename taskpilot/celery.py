import os
from celery import Celery

# Ensure settings module is set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskpilot.settings")

app = Celery("taskpilot")

# Load settings from Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks inside Django apps
app.autodiscover_tasks()

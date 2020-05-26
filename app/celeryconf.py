import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

celery_app = Celery('app')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "task_update_status_of_articles": {
        "task": "app.core.tasks.task_update_status_of_articles",
        "schedule": 5.0,
        "args": None
    }
}

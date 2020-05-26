
from celery.decorators import task
from celery.utils.log import get_task_logger

from ..publication.models import Article

logger = get_task_logger(__name__)


@task
def task_update_status_of_articles():
    """The CronJob Function to update status to review"""
    Article.objects.change_status_to_review()

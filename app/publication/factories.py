from factory.django import DjangoModelFactory
import factory
import random

from .models import Article, Author
from . import ArticleChoices

from ..core.factories import UserFactory


def retrieve_availability_status_choices():
    """This method will return randomly the article choices"""
    choices = [x[0] for x in ArticleChoices.AVAILABILITY_CHOICES]
    return random.choice(choices)


def retrieve_status_choices():
    """this method will retrieve article status choices"""

    choices = [x[0] for x in ArticleChoices.ARTICLE_STATUSES]
    return random.choice(choices)


class ArticleFactory(DjangoModelFactory):
    """This factory is for article model"""

    class Meta:
        model = Article

    name = factory.Faker("first_name")
    availability_status = factory.LazyFunction(retrieve_availability_status_choices)
    status = factory.LazyFunction(retrieve_status_choices)
    google_doc_link = factory.Faker("sentence")


class AuthorFactory(DjangoModelFactory):
    """ Factory of models.Author """

    class Meta:
        model = Author

    user = factory.SubFactory(UserFactory)
    article = factory.SubFactory(ArticleFactory)


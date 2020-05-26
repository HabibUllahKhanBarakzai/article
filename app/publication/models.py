
from typing import AnyStr

from django.db import models
from django.conf import settings

from . import ArticleChoices
from ..core.models import User


class AbstractDateModel(models.Model):
    """Abstract model to keep Date Records"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ArticleQuerySet(models.QuerySet):
    """Custom QuerySet for articles"""
    def create_article_with_author(
            self,
            user: User,
            name: AnyStr,
            google_doc_link: AnyStr = None,
            status=ArticleChoices.IN_PROGRESS
    ):

        """creating article and corresponding Author object"""
        article = self.create(name=name, status=status, google_doc_link=google_doc_link)
        author = Author(user=user, article=article)
        author.save()

        return {"article": article, "author": author}

    def change_status_to_review(self):
        """This method is basically created for cronJob to see all the object that have google link
        and are open, change their status to IN REVIEW"""
        self.filter(google_doc_link__isnull=False,
                    availability_status=ArticleChoices.OPEN
                    ).update(status=ArticleChoices.REVIEW)


class Article(AbstractDateModel):
    """main article model for publication, Every Event of an article will be
       save in this model's parameter field"""

    name = models.CharField(max_length=settings.DEFAULT_MAX_CHAR_LENGTH)

    availability_status = models.CharField(
        max_length=settings.DEFAULT_MAX_CHAR_LENGTH,
        choices=ArticleChoices.AVAILABILITY_CHOICES,
        default=ArticleChoices.OPEN
    )

    status = models.CharField(max_length=settings.DEFAULT_MAX_CHAR_LENGTH,
                              choices=ArticleChoices.ARTICLE_STATUSES,
                              default=ArticleChoices.STARTED)

    google_doc_link = models.URLField(null=True, max_length=500)

    authors = models.ManyToManyField(User,
                                     related_name="articles",
                                     through="publication.Author",
                                     through_fields=('article', 'user'))

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.name


class Author(AbstractDateModel):
    """Many to Many Field Through model it will save what parameters were
       passed to change the Article object"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="article_events"
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="article_events"
    )

    class Meta:
        unique_together = (('user', 'article'), )

    def __str__(self):
        return f"{self.user.__str__()} :: {self.article.__str__()}"

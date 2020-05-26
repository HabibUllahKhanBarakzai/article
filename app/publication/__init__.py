
class ArticleChoices:
    """Statuses of article"""

    STARTED = "started"
    IN_PROGRESS = "in_progress"
    REVIEW = "in_review"
    DONE = "done"
    PUBLISHED = "published"

    ARTICLE_STATUSES = (
        (STARTED, "Writer has started work"),
        (IN_PROGRESS, "Article is in progress"),
        (REVIEW, "Editor is reviewing the article"),
        (DONE, "Article is reviewed and marked done"),
        (PUBLISHED, "Article is published")
    )

    OPEN = "open"
    CLOSED = "closed"

    AVAILABILITY_CHOICES = (
        (OPEN, "article is open, and can be changed"),
        (CLOSED, "article is closed, cannot be changed")
    )

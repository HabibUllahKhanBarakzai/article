
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Author
from .serializers import ArticleSerializer

from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    """Checking permissions for Writer and Editor"""
    def has_permission(self, request, view):
        """Checking Permissions, basically editor can only review article,
         he cannot create article"""
        return False if request.method.lower() == "post" and request.user.is_editor else True


class ArticleViewSet(ModelViewSet):
    """main view to create article"""
    queryset = Article.objects.all()
    permission_classes = (UserPermissions, )
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        created_objects = Article.objects.create_article_with_author(
            user=request.user,
            name=request.data.get("name"),
            google_doc_link=request.data.get("google_doc_link")
        )

        response = self.serialize_article_object(created_objects['author'])
        return Response(response,
                        status=status.HTTP_201_CREATED)

    @classmethod
    def serialize_article_object(cls, article: Article) -> dict:
        return dict(
            name=article.name,
            status=article.status,
            availibility_status=article.availability_status,
            google_doc_link=article.google_doc_link
        )
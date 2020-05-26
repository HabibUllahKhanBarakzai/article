from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Article, Author
from ..core.models import User


class AuthorSerializer(ModelSerializer):
    """Nested Serializer for many to many field"""

    class Meta:
        model = User
        fields = ("email", "last_name", "first_name", "id")


class ArticleSerializer(ModelSerializer):
    """Serializer Field for Article Model"""
    authors = AuthorSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Article
        fields = "__all__"

    def update(self, instance, validated_data):
        """Custom Update Method, Creates an Author instance as well"""
        instance = super(self.__class__, self).update(instance, validated_data)

        author, _ = Author.objects.get_or_create(
            user=self.context['request'].user,
            article=instance
        )
        return instance

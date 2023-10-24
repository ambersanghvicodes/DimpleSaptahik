from rest_framework import serializers
from .models import Article, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Author
        fields = ('name')

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField()
    class Meta():
        model = Article
        fields = '__all__'
        extra_fields = ['author_name']
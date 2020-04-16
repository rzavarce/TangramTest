from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
	"""
    API endpoint that allows users to be viewed or edited.
    """


	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = Article
		fields = ['id', 'art_title', 'art_content', 'art_status']












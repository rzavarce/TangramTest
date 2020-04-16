from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
	"""
    API endpoint that allows users to be viewed or edited.
    """


	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = Author
		fields = ['id', 'aut_name', 'aut_email', 'aut_status']












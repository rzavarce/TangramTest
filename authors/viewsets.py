from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer



class AuthorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Author.objects.filter(aut_status=1)
	serializer_class = AuthorSerializer
	ordering_fields = ('id',)
	ordering = ('id',)



	def create(self, request):

		serializer = AuthorSerializer(data=request.data)

		if serializer.is_valid():
			author = Author()
			author.aut_name = serializer.validated_data['aut_name']
			author.aut_email = serializer.validated_data['aut_email']
			author.aut_status = serializer.validated_data['aut_status']
			author.aut_created_date = timezone.now()
			author.aut_modified_date = timezone.now()
			author.aut_creator = request.user

			author.save()

			queryset = Author.objects.all()
			serializer = AuthorSerializer(queryset, many=True)

			return Response(serializer.data)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		
	def update(self, request, pk=None):

		serializer = AuthorSerializer(data=request.data)

		if serializer.is_valid():
			author = Author.objects.get(pk=pk)
			author.aut_name = serializer.validated_data['aut_name']
			author.aut_email = serializer.validated_data['aut_email']
			author.aut_status = serializer.validated_data['aut_status']			
			author.aut_modified_date = timezone.now()

			author.save()

			return serializer
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer



class ArticleViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	ordering_fields = ('-id',)
	ordering = ('-id',)



	def create(self, request):

		serializer = ArticleSerializer(data=request.data)

		if serializer.is_valid():
			article = Article()
			article.art_title = serializer.validated_data['art_title']
			article.art_content = serializer.validated_data['art_content']
			article.art_status = serializer.validated_data['art_status']
			article.art_created_date = timezone.now()
			article.art_modified_date = timezone.now()
			article.art_creator = request.user

			article.save()

			queryset = Article.objects.all()
			serializer = ArticleSerializer(queryset, many=True)

			return Response(serializer.data)

		else:
			return Response(serializer.errors,)

		
	def update(self, request, pk=None):

		serializer = ArticleSerializer(data=request.data)

		if serializer.is_valid():
			article = Article.objects.get(pk=pk)
			article.art_title = serializer.validated_data['art_title']
			article.art_content = serializer.validated_data['art_content']
			article.art_status = serializer.validated_data['art_status']			
			article.art_modified_date = timezone.now()

			article.save()

			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










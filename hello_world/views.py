from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Posts
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostPossesor
from rest_framework import filters
from .filters import postFilter
from django_filters.rest_framework import DjangoFilterBackend

class HelloWorldView(APIView):
	def get(self, request):
		return Response({"hi": 'this is my first rest_framework work'})


class PostView(ModelViewSet):
	permission_classes=[IsAuthenticated, IsPostPossesor]
	queryset=Posts.objects.all()
	serializer_class = PostSerializer

	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filter_class = postFilter
	ordering_fields = ['id']
	search_fields=['title', 'content']

	def get_queryset(self):
		return Posts.objects.filter(author = self.request.user)

from django.shortcuts import render
from .serializers import PostsSerializer
from .models import Post
from rest_framework import viewsets

# Create your views here.
class PostViewSets(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
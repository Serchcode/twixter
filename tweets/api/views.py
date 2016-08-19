from rest_framework import generics
from ..models import Tweet
from .serializers import TweetSerializer

class TweetListView(generics.ListAPIView):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer

class TweetDetailView(generics.RetrieveAPIView):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer
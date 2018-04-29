from rest_framework import generics
from .serializers import TweetSerializer
from tweet.models import TweetModel
from django.utils import timezone
class TweetListAPIView(generics.ListAPIView):
	queryset =TweetModel.objects.all()
	serializer_class = TweetSerializer


class TweetCreateAPIView(generics.CreateAPIView):
	#
	serializer_class =TweetSerializer
	
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)


class TweetDetailAPIView(generics.RetrieveAPIView):
	queryset = TweetModel.objects.all()
	serializer_class = TweetSerializer
from rest_framework import serializers
from tweet.models import TweetModel
from django.contrib.auth.models import User


class UserDisplaySerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields=('username',)

class TweetSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)
	timestamp = serializers.DateTimeField(source='FORMAT',read_only=True)
	class Meta:
		model = TweetModel
		ordering=['-id',]
		fields =('pk','user','content','timestamp')




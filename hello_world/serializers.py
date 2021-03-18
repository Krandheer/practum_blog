from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):

	author = serializers.CharField(source = 'author.username', read_only = True)
	class Meta:
		model = Posts
		fields='__all__'
		read_only_fields=('author',)

			
	def create(self, validated_data):
		validated_data['author']=self.context['request'].user
		return Posts.objects.create(**validated_data)
from rest_framework import serializers
from .models import*

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['title','image','content','tags']

    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields=['title','content','tags']
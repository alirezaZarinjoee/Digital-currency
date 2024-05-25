from rest_framework import serializers
from .models import *
from django.urls import reverse
#-------------------------------------------------------------------
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields='__all__'
#-------------------------------------------------------------------

class BlogSerializers(serializers.ModelSerializer):
    images=GallerySerializer(many=True,read_only=True)

    class Meta:
        model=Blog
        fields='__all__'
    #     read_only_fields = ['absolute_url']
    
    # absolute_url = serializers.SerializerMethodField()
    # def get_absolute_url(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(reverse('blog:detail_blog', args=[obj.slug]))
#-------------------------------------------------------------------

class WriterSerializer(serializers.ModelSerializer):
    blogs=BlogSerializers(many=True,read_only=True)
    class Meta:
        model=Writer
        fields=['id','full_name','email','image']

#-------------------------------------------------------------------

class GoupBlogSerializer(serializers.ModelSerializer):
    blogs=BlogSerializers(many=True,read_only=True)
    class Meta:
        model=GroupBlog
        fields='__all__'
#-------------------------------------------------------------------

from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import utils
# Create your models here.
class Writer(models.Model):
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    is_active=models.BooleanField(default=True)
    image_upload=utils.FileUpload('images','writer')
    image=models.ImageField(upload_to=image_upload.upload_to,null=True,blank=True,default='images/nophoto.jpeg')
    slug=models.SlugField(null=True,blank=True,unique=True)

    def save(self, *args, **kwargs): #function for save slug from fields
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
    
    
    class Meta:
        verbose_name='writer'
        verbose_name_plural='writers'

#------------------------------------------------------
class GroupBlog(models.Model):
    group_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    slug=models.SlugField(null=True,blank=True,unique=True)

    def save(self, *args, **kwargs): #function for save slug from fields
        if not self.slug:
            self.slug = slugify(self.group_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.group_name
    
    class Meta:
        verbose_name='group_blog'
        verbose_name_plural='group_blogs'

#----------------------------------------------------

class Blog(models.Model):
    blog_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)
    short_description=models.TextField()
    long_description=models.TextField()
    image_upload=utils.FileUpload('images','blog')
    image=models.ImageField(upload_to=image_upload.upload_to,null=True,blank=True)
    image=models.ImageField(upload_to='')
    register_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)
    group=models.ForeignKey(GroupBlog, on_delete=models.CASCADE,related_name='blogs')
    writer=models.ForeignKey(Writer,on_delete=models.CASCADE,related_name='blogs')
    slug=models.SlugField(null=True,blank=True,unique=True)

    
    def save(self, *args, **kwargs): #function for save slug from fields
        if not self.slug:
            self.slug = slugify(self.blog_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_name
    
    class Meta:
        verbose_name='blog'
        verbose_name_plural='blogs'

#----------------------------------------------
class Gallery(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='images')
    image_upload=utils.FileUpload('images','gallrey',f'{blog}')
    image=models.ImageField(upload_to=image_upload.upload_to)
    
    
    class Meta:
        verbose_name='photo'
        verbose_name_plural='photos'
        

from email.policy import default
from turtle import title
from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Project(models.Model):
    owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    
    featured_image=models.ImageField(blank=True,null=True, default='default.jpg')
    tags=models.ManyToManyField('Tag',blank=True)
    demo_link=models.CharField(max_length=2000, blank=True)
   
    source_link=models.CharField(max_length=2000, blank=True,null=True)
    vote_total=models.TextField(blank=True,null=True,default=0)
    vote_ratio=models.TextField(blank=True,null=True,default=0)
    
    created=models.DateTimeField(auto_now_add=True)#automatically create timestamp
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    
    def __str__(self):
        return self.title #to make the title show in the admin page after addition
    
    
    
class Review(models.Model):
    VOTE_TYPE=[
        ('up','Up vote'),
        ('down','Down vote'),
    ]
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)#automatically create timestamp
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)#automatically create timestamp
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return self.name
    
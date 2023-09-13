from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import date , datetime
# Create your models here.

class Notes(models.Model):
    title= models.CharField(max_length=255)
    header_image =models.ImageField(null=True ,blank=True , upload_to="images/")
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=500)
    text= RichTextField(blank=True , null=True)
    Note_date = models.DateField(auto_now_add=True)
    # text= models.TextField()
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        # return reverse('article-detail',args=(str(self.id)))
        return reverse('home')
    @property
    def has_header_image(self):
        return bool(self.header_image)

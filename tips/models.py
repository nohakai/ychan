from django.db import models
from django.utils import timezone



class Topic(models.Model):
    user = models.CharField(max_length=50, blank=False, null=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.CharField(max_length=50,blank=False, null=True)
    comment = models.TextField('')
    img = models.ImageField(blank=True, null=True)
    target = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='対象スレッド')
    created_at = models.DateTimeField('日時', auto_now_add=True)

    def __str__(self):
        return self.comment[:20]
    
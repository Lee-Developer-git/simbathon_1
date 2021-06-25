from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    body=models.TextField()
    tag=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:20]

class Vlog(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    body=models.TextField()
    tag=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:20]
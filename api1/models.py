from django.db import models


class Post(models.Model):
 Author_Name = models.CharField(max_length=50)
 Author_id = models.IntegerField()
 Book_Name = models.CharField(max_length=50)
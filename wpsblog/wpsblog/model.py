from django.db import models

class Post(models.Model):
    title = models.CharField(
        mas_length=120,
    )
	content = models.TextField()
    
	def __str__(self):
        return self.title

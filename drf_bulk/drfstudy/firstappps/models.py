from django.db import models

# Create your models here.

class Post(models.Model):

    post_name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    update_at = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.id) + self.post_name
from django.db import models
from users.models import User

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
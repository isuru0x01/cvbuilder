```python
from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.title
```
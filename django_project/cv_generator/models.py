```python
from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv_file = models.FileField(upload_to='cv_files/')
    cover_letter = models.FileField(upload_to='cover_letter_files/')
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()

    def __str__(self):
        return self.user.username

class LaTeXTemplate(models.Model):
    template_name = models.CharField(max_length=200)
    template_file = models.FileField(upload_to='latex_templates/')

    def __str__(self):
        return self.template_name
```
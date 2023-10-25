```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields in here
    cv = models.FileField(upload_to='cv_files/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='cover_letter_files/', null=True, blank=True)
```

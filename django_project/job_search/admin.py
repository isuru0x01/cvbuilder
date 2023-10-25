```python
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'company_name', 'post_date')
    search_fields = ('title', 'location', 'company_name')
    ordering = ('-post_date',)
```
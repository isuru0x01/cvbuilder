```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('cv_generator/', include('cv_generator.urls')),
    path('job_search/', include('job_search.urls')),
]
```
```python
from django.urls import path
from . import views

app_name = 'cv_generator'

urlpatterns = [
    path('upload_cv/', views.upload_cv, name='upload_cv'),
    path('generate_cv/', views.generate_cv, name='generate_cv'),
]
```
```python
from django.urls import path
from . import views

app_name = 'job_search'

urlpatterns = [
    path('', views.JobSearchView.as_view(), name='job_search'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('apply/<int:pk>/', views.ApplyJobView.as_view(), name='apply_job'),
]
```
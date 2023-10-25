```python
from django.shortcuts import render
from .models import Job
from .forms import JobSearchForm
import requests

def job_search(request):
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            job_title = form.cleaned_data['job_title']
            location = form.cleaned_data['location']
            # Call Google Search API
            response = requests.get(f'https://www.googleapis.com/customsearch/v1?q={job_title}+in+{location}')
            jobs = response.json()
            # Save jobs to database
            for job in jobs['items']:
                Job.objects.create(
                    title=job['title'],
                    link=job['link'],
                    snippet=job['snippet']
                )
            return render(request, 'job_search_results.html', {'jobs': jobs['items']})
    else:
        form = JobSearchForm()
    return render(request, 'job_search.html', {'form': form})

def job_description(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job_description.html', {'job': job})
```
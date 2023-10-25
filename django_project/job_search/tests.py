```python
from django.test import TestCase
from django.urls import reverse
from .models import Job

class JobSearchTest(TestCase):

    def setUp(self):
        self.job = Job.objects.create(
            title='Software Engineer',
            location='New York',
            company='Google',
            description='A great job opportunity for software engineers.',
            url='https://www.google.com/jobs/softwareengineer'
        )

    def test_job_listing_page(self):
        response = self.client.get(reverse('job_search'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Engineer')
        self.assertContains(response, 'New York')
        self.assertContains(response, 'Google')

    def test_job_detail_page(self):
        response = self.client.get(reverse('job_description', args=(self.job.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Engineer')
        self.assertContains(response, 'New York')
        self.assertContains(response, 'Google')
        self.assertContains(response, 'A great job opportunity for software engineers.')
        self.assertContains(response, 'https://www.google.com/jobs/softwareengineer')
```
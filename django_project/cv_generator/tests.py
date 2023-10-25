```python
from django.test import TestCase
from django.contrib.auth.models import User
from .models import CV, CoverLetter

class CVTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cv = CV.objects.create(user=self.user, title='Test CV', content='This is a test CV')

    def test_cv_creation(self):
        self.assertEqual(self.cv.title, 'Test CV')
        self.assertEqual(self.cv.content, 'This is a test CV')
        self.assertEqual(self.cv.user, self.user)

class CoverLetterTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cover_letter = CoverLetter.objects.create(user=self.user, title='Test Cover Letter', content='This is a test cover letter')

    def test_cover_letter_creation(self):
        self.assertEqual(self.cover_letter.title, 'Test Cover Letter')
        self.assertEqual(self.cover_letter.content, 'This is a test cover letter')
        self.assertEqual(self.cover_letter.user, self.user)
```
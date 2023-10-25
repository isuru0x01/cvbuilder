```python
from django import forms

class JobSearchForm(forms.Form):
    job_title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
```
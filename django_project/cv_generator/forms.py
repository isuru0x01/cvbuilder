```python
from django import forms
from .models import CV, CoverLetter

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['title', 'description', 'cv_file']

    def clean_cv_file(self):
        cv_file = self.cleaned_data.get('cv_file')
        if cv_file:
            if cv_file.size > 5*1024*1024:
                raise forms.ValidationError("The maximum file size that can be uploaded is 5MB")
            if not cv_file.content_type in ["application/pdf", "application/msword"]:
                raise forms.ValidationError("Content type is not a PDF or Word document")
        else:
            raise forms.ValidationError("Couldn't read uploaded document")
        return cv_file

class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = ['title', 'description', 'cover_letter_file']

    def clean_cover_letter_file(self):
        cover_letter_file = self.cleaned_data.get('cover_letter_file')
        if cover_letter_file:
            if cover_letter_file.size > 5*1024*1024:
                raise forms.ValidationError("The maximum file size that can be uploaded is 5MB")
            if not cover_letter_file.content_type in ["application/pdf", "application/msword"]:
                raise forms.ValidationError("Content type is not a PDF or Word document")
        else:
            raise forms.ValidationError("Couldn't read uploaded document")
        return cover_letter_file
```
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CVForm, CoverLetterForm
from .models import CV, CoverLetter
from .utils import generate_cv, generate_cover_letter

@login_required
def upload_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            return redirect('cv_generator:generate_cv')
    else:
        form = CVForm()
    return render(request, 'upload_cv.html', {'form': form})

@login_required
def upload_cover_letter(request):
    if request.method == 'POST':
        form = CoverLetterForm(request.POST, request.FILES)
        if form.is_valid():
            cover_letter = form.save(commit=False)
            cover_letter.user = request.user
            cover_letter.save()
            return redirect('cv_generator:generate_cover_letter')
    else:
        form = CoverLetterForm()
    return render(request, 'upload_cover_letter.html', {'form': form})

@login_required
def generate_cv(request):
    user_cv = CV.objects.filter(user=request.user).first()
    if user_cv:
        cv_content = generate_cv(user_cv)
        return render(request, 'generate_cv.html', {'cv_content': cv_content})
    else:
        return redirect('cv_generator:upload_cv')

@login_required
def generate_cover_letter(request):
    user_cover_letter = CoverLetter.objects.filter(user=request.user).first()
    if user_cover_letter:
        cover_letter_content = generate_cover_letter(user_cover_letter)
        return render(request, 'generate_cover_letter.html', {'cover_letter_content': cover_letter_content})
    else:
        return redirect('cv_generator:upload_cover_letter')
```
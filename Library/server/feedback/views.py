from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'feedback/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {
        'form': form,
        'title': 'Связь с нами',
        'link_list': ['server/css/crud.css'],
    })

from django.shortcuts import render
from .models import job_posting
# Create your views here.
def index(request):
    active_postings = job_posting.objects.filter(is_active = True)
    context = {
        'job_postings': active_postings
    }
    return render(request, 'job_board/index.html', context)
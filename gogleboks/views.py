from django.shortcuts import render
from django.utils import timezone
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'gogleboks/review_list.html', {'reviews':reviews})

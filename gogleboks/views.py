from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'gogleboks/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'gogleboks/review_detail.html', {'review':review})

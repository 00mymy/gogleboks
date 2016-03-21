from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
from .gbapi import getGogleBokSearch, getGogleBokDetail

# Create your views here.
def review_list(request, bid):
    reviews = Review.objects.filter(book=bid).order_by('published_date')
    return render(request, 'gogleboks/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'gogleboks/review_detail.html', {'review':review})

def review_new(request, bid):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = bid
            review.author = request.user
            review.created_date = timezone.now()
            review.published_date = timezone.now()
            review.save()
            return redirect('gogleboks.views.book_detail',bid=bid)
    else:
        form = ReviewForm()
    return render(request, 'gogleboks/review_edit.html', {'form':form})

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.published_date = timezone.now()
            review.save()
            return redirect('gogleboks.views.book_detail', bid=review.book)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'gogleboks/review_edit.html', {'form': form})

def book_search(request):
    q = ''
    if 'q' in request.GET:
        q = request.GET['q']

    s_result = getGogleBokSearch(q)
    return render(request, 'gogleboks/search_result.html', {'q':q, 's_result': s_result} )

def book_detail(request, bid):
    book = getGogleBokDetail(bid=bid)
    reviews = Review.objects.filter(book=bid).order_by('published_date')
    return render(request, 'gogleboks/book_detail.html', {'book':book, 'reviews':reviews})

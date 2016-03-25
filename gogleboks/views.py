from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
from .gbapi import *

# Create your views here.
def review_list(request):
    reviews = Review.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'gogleboks/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'gogleboks/review_detail.html', {'review':review})

def review_new(request, bid):
    book = getGogleBokDetail(bid=bid)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.bid = bid
            review.title = book['volumeInfo']['title']
            if 'subtitle' in book['volumeInfo']:
                review.subtitle = book['volumeInfo']['subtitle']
            review.authors = book['volumeInfo']['authors']
            review.created_date = timezone.now()
            review.updated_date = timezone.now()
            review.score = request.POST['score']
            review.save()
            return redirect('gogleboks.views.book_detail',bid=bid)
    else:
        form = ReviewForm()
    return render(request, 'gogleboks/review_edit.html', {'form':form, 'title':book['volumeInfo']['title']})

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.updated_date = timezone.now()
            review.score = request.POST['score']
            review.save()
            return redirect('gogleboks.views.book_detail', bid=review.bid)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'gogleboks/review_edit.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('gogleboks.views.book_detail', bid=review.bid)

def book_search(request):
    q = ''
    if 'q' in request.GET:
        q = request.GET['q']

    s_result = getGogleBokSearch(q)
    return render(request, 'gogleboks/search_result.html', {'q':q, 's_result': s_result} )

def book_detail(request, bid):
    book = getGogleBokDetail(bid=bid)
    reviews = Review.objects.filter(bid=bid).order_by('-created_date')
    if 'authors' in book['volumeInfo'].keys():
        morebooks = getGogleBokSearchMoreabout('"' + book['volumeInfo']['title'] + '"+' + '+'.join(book['volumeInfo']['authors']) + '"')
    else:
        morebooks = None
    return render(request, 'gogleboks/book_detail.html', {'book':book, 'reviews':reviews, 'morebooks':morebooks})
    #return render(request, 'gogleboks/book_detail.html', {'book':book, 'reviews':reviews})

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Review
from .forms import *
from .gbapi import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

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
    return render(request, 'gogleboks/review_edit.html', {'form': form, 'title':review.title, 'score':review.score})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('gogleboks.views.book_detail', bid=review.bid)

def book_search(request, sx=0):
    q = ''

    if 'q' in request.GET:
        q = request.GET['q']

    if 'sx' in request.GET:
        sx = int(request.GET['sx'])

    s_result = getGogleBokSearch(q, sx)
    return render(request, 'gogleboks/search_result.html', {'q':q, 'sx':sx, 's_result': s_result} )

def book_detail(request, bid):
    book = getGogleBokDetail(bid=bid)
    reviews = Review.objects.filter(bid=bid).order_by('-created_date')
    if 'authors' in book['volumeInfo'].keys():
        morebooks = getGogleBokSearchMoreabout('"' + book['volumeInfo']['title'] + '"+' + '+'.join(book['volumeInfo']['authors']) + '"')
    else:
        morebooks = None
    return render(request, 'gogleboks/book_detail.html', {'book':book, 'reviews':reviews, 'morebooks':morebooks})
    #return render(request, 'gogleboks/book_detail.html', {'book':book, 'reviews':reviews})

def book_viewer(request, bid):
    return render(request, 'gogleboks/book_viewer.html', {'bid':bid})

'''
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            #return HttpResponseRedirect('/register/success/')
            return HttpResponseRedirect('/accounts/login/?reg_ok=Y')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {
            'form': form
            })

        return render_to_response(
            'registration/register.html',
            variables,
            )

def reg_edit(request):
    user = request.user
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.username = 'xxx'
        if form.is_valid():
            print('3. =============================')
            #user = form.save(commit=False)
            #user.username = form.cleaned_data['username']
            user = User.objects.get(pk=user.id)
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password1']
            print('4. =============================')
            user.save()
            print('5. =============================')
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm(instance=user)
        #return render(request, 'registration/register.html', {'form': form})
        variables = RequestContext(request, {
                    'form': form
                    })
        return render_to_response('registration/register.html', variables,)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
'''

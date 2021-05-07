from django.db.models import query
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import shorturl
import random
import string

# Create your views here.

def home(request):
    return HttpResponse("<h1>THIS IS THE HOMEPAGE</h1>")

def ok(request):
    return render(request, 'base.html')

def generate_random_shorturl(length):
    # base 62 conversion - [A-Z][a-z][0-9]  
    random_key = ''.join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length)
        )
    return random_key

def generate(request):
    if request.method == "POST":
        #generate short url based on user input
        if request.POST['original'] and request.POST['short']:
            original = request.POST['original'] 
            short = request.POST['short'] 
            exists = shorturl.objects.filter(short_url = short)

            if not exists:
                # create a new short url based on user input
                new_url = shorturl(
                    original_url = original,
                    short_url = short,
                )
                new_url.save()

                query = shorturl.objects.filter(short_url = short)
                context = {'urls' : query, 'succesfully_generated' : True}

                return render(request, 'index.html', context)
                # return redirect('/test')
            else:
                messages.error(request, "Already Exists")
                return redirect('/test')

        # generate short url randomly
        elif request.POST['original']:
            original = request.POST['original']
            short = generate_random_shorturl(7)
            exists = shorturl.objects.filter(short_url = short)

            if not exists:
                # create a new short url based on user input
                new_url = shorturl(
                    original_url = original,
                    short_url = short,
                )
                new_url.save()

                query = shorturl.objects.filter(short_url = short)
                context = {'urls' : query, 'succesfully_generated' : True}

                return render(request, 'index.html', context)
                # return redirect('/test')
            else:
                messages.error(request, "Already Exists")
                return redirect('/test')
        else:
            messages.error(request, "Please enter the link")
            return redirect('/test')
    else:
        return redirect('/')

def test(request):
    # query = shorturl.objects.all()
    # context = {'urls' : query}
    return render(request, 'index.html')

def stats(short_url):
    query = shorturl.objects.all()
    for q in query:
        target = q.short_url.filter(short_url)
        print(target)



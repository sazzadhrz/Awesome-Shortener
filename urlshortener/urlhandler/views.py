from django.db.models import query
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404

from .models import shorturl
import random
import string

# Create your views here.

# def ok(request):
#     return render(request, 'base.html')

def generate_random_shorturl(length):
    # base 62 conversion - [A-Z][a-z][0-9]  
    random_key = ''.join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length)
        )
    return random_key

succesfully_generated = False

def create_new_shorturl_object(request, original, short, random=False):
    '''
    Creates a new shorturl object if short_url doesn't exist. If exists, redirect to homepage.
    Parameters:
        request - request
        original - original url that needs to be shortened
        short - short url of the original url
    '''
    
    global succesfully_generated
    exists = shorturl.objects.filter(short_url = short)

    # handles if random key already exists
    if random and exists:
        short = generate_random_shorturl(7)
        create_new_shorturl_object(request, original=original, short=short, random=True)

    if not exists:
        # create a new short url based on user input
        new_url = shorturl(
            original_url = original,
            short_url = short,
        )
        new_url.save()
        succesfully_generated = True
    else:
        succesfully_generated = False
        messages.error(request, "Already Exists")
        return redirect('/')

def generate(request):
    global succesfully_generated
    if request.method == "POST":
        #generate short url based on user input
        if request.POST['original'] and request.POST['short']:
            original = request.POST['original'] 
            short = request.POST['short'] 
            
            create_new_shorturl_object(request, original=original, short=short)

            query = shorturl.objects.filter(short_url = short)
            context = {'urls' : query, 'succesfully_generated' : succesfully_generated}

            return render(request, 'index.html', context)
        

        # generate short url randomly
        elif request.POST['original']:
            original = request.POST['original']
            short = generate_random_shorturl(7)

            create_new_shorturl_object(request, original=original, short=short, random=True)

            query = shorturl.objects.filter(short_url = short)
            context = {'urls' : query, 'succesfully_generated' : succesfully_generated}

            return render(request, 'index.html', context)

        else:
            messages.error(request, "Please enter the link")
            return redirect(home)
    else:
        return redirect(home)

# def test(request):
#     # query = shorturl.objects.all()
#     # context = {'urls' : query}
#     return render(request, 'index.html')

def home (request):
    # return HttpResponse("<h1>THIS IS THE HOMEPAGE</h1>")
    return render(request, 'index.html')

def show(request, short_url):
    try:
        exists = shorturl.objects.get(short_url=short_url)
        exists.visits += 1
        exists.save()
        return redirect(exists.original_url)
    except:
        return render(request, '404.html')

def stats(request, short_url):
    try:
        exists = shorturl.objects.get(short_url=short_url)
        context = {'query' : exists}
        return render(request, 'stats.html', context)
    except:
        return render(request, '404.html')



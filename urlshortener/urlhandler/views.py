from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ShortURL
import random
import string

# Create your views here.

SHORTURL_LEN = 7
succesfully_generated = False


def generate_random_shorturl(length):
    ''' Generates a random short URL key of given length'''
    # base 62 conversion - [A-Z][a-z][0-9]  
    
    random_key = ''.join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length)
        )
    return random_key


def create_new_shorturl_object(request, original, short, random=False):
    '''
    Creates a new ShortURL object if short_url doesn't exist. If exists, redirect to homepage.
    Parameters:
        request - request
        original - original url that needs to be shortened
        short - short url of the original url
    '''
    
    global succesfully_generated
    exists = ShortURL.objects.filter(short_url = short)

    # handles if random key already exists
    if random and exists:
        short = generate_random_shorturl(SHORTURL_LEN)
        create_new_shorturl_object(request, original=original, short=short, random=True)

    if not exists:
        # create a new short url based on user input
        new_url = ShortURL(
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
    ''' Generates Short URL based on user input. If no input provided, it generates random URL'''

    global succesfully_generated

    if request.method == "POST":
        #generate short url based on user input
        if request.POST['original'] and request.POST['short']:
            original = request.POST['original'] 
            short = request.POST['short'] 
            
            create_new_shorturl_object(request, original=original, short=short)

            query = ShortURL.objects.filter(short_url = short)
            context = {'urls' : query, 'succesfully_generated' : succesfully_generated}

            return render(request, 'index.html', context)
        

        # generate short url randomly
        elif request.POST['original']:
            original = request.POST['original']
            short = generate_random_shorturl(SHORTURL_LEN)

            create_new_shorturl_object(request, original=original, short=short, random=True)

            query = ShortURL.objects.filter(short_url = short)
            context = {'urls' : query, 'succesfully_generated' : succesfully_generated}

            return render(request, 'index.html', context)

        else:
            messages.error(request, "Please enter the link")
            return redirect(home)
    else:
        return redirect(home)



def home (request):
    ''' Renders the homepage '''
    return render(request, 'index.html')



def show(request, short_url):
    ''' If short URL is already created, redirects to the original URL and updates the visit count '''
    try:
        exists = ShortURL.objects.get(short_url=short_url)
        exists.visits += 1
        exists.save()
        return redirect(exists.original_url)
    except:
        return render(request, '404.html')



def stats(request, short_url):
    ''' Responsible for short URLs statistical data representation '''
    try:
        exists = ShortURL.objects.get(short_url=short_url)
        context = {'query' : exists}
        return render(request, 'stats.html', context)
    except:
        return render(request, '404.html')


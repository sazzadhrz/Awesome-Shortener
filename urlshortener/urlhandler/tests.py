from django import test
from django.test import TestCase

from .views import generate_random_shorturl
from .models import ShortURL

# Create your tests here.

class URLGenerationTestCase(TestCase):
    def test_length(self):
        for i in range(10):
            key = generate_random_shorturl(i)
            self.assertEqual(len(key), i)
    
    def test_negative_length(self):
        key = generate_random_shorturl(-5)
        self.assertEqual(len(key), 0)

class ModelTestCase(TestCase):
    def setUp(self):
        ShortURL.objects.create(
            original_url='https://www.google.com/',
            short_url = 'google5'
        )
        ShortURL.objects.create(
            original_url='https://www.youtube.com/',
            short_url = 'y8XE5g0'
        )

    def test_url_to_redirect(self):
        google = ShortURL.objects.get(short_url = 'google5')
        youtube = ShortURL.objects.get(short_url = 'y8XE5g0')
        self.assertEqual(google.original_url, 'https://www.google.com/')
        self.assertEqual(youtube.original_url, 'https://www.youtube.com/')
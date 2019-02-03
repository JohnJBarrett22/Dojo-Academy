from django.test import TestCase, Client
from .models import Album

class AlbumTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Album.objects.create(title = "Enter the Wu Tang", artist = "Wu Tang", year = 1993)

    def test_hello(self):
        print("I am in Django!")

    def test_urls(self):
        c = Client()
        res = c.get('/')
        print(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(c.get('/add').status_code, 302)
        self.assertEqual(c.get('/delete').status_code, 302)
        self.assertEqual(c.get('/edit').status_code, 302)

    def test_model_creation(self):
        a = Album.objects.create(title = "Dark Side of the Moon", artist = "Pink Floyd", year = 1973)
        self.assertEqual(a.title, "Dark Side of the Moon")
        self.assertEqual(a.artist, "Pink Floyd")
        self.assertEqual(a.year, 1973)

    def test_get_album_model(self):
        a = Album.objects.get(id = 1)
        print(a)
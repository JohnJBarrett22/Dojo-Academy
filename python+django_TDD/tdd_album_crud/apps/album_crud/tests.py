from django.test import TestCase, Client
from .models import Album

class AlbumTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Album.objects.create(title = "Enter the Wu Tang", artist = "Wu Tang", year = 1993)
        Album.objects.create(title = "I Don't Know", artist = "Alanais Morissette", year = 1993)

    def test_hello(self):
        print("I am in Django!")

    def test_urls(self):
        c = Client()
        res = c.get('/')
        print(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(c.get('/add').status_code, 302)
        self.assertEqual(c.get('/delete').status_code, 302)
        self.assertEqual(c.get('/edit/1').status_code, 200)

    def test_model_creation(self):
        a = Album.objects.create(title = "Dark Side of the Moon", artist = "Pink Floyd", year = 1973)
        self.assertEqual(a.title, "Dark Side of the Moon")
        self.assertEqual(a.artist, "Pink Floyd")
        self.assertEqual(a.year, 1973)

    def test_get_album_model(self):
        a = Album.objects.get(id = 1)
        self.assertEqual(a.id, 1)
        # self.assertEqual(Album.objects.get(title = "Enter the Wu Tang").title, "Enter the Wu Tang")
        albums = Album.objects.filter(year = 1993).values("year")
        for album in albums:
            self.assertEqual(album["year"], 1993)

    # Integration Test
    def test_view_creation(self):
        c = Client()
        post_data = {
            "title" : "Debut",
            "artist" : "Bjork",
            "year" : 1993
        }
        res = c.post('/add', post_data)
        self.assertEqual(res.status_code, 302)
        a = Album.objects.last()
        self.assertEqual(a.title, post_data["title"])
        self.assertEqual(a.artist, post_data["artist"])
        self.assertEqual(a.year, post_data["year"])

    def test_view_edit(self):
        c = Client()
        post_data = {
            "title": "A Test Edit",
            "artist" : "Test Artist Edit",
            "year": 3099
        }
        # This should edit the single album that is created by our setUp method
        response = c.post('/album/1/edit', post_data)
        # Let's make sure the view function eventually redirects
        self.assertEqual(response.status_code, 302)
        # Let's test to make sure the edit worked
        edited = Album.objects.get(id = 1)
        self.assertEqual(edited.title, post_data['title'])
        self.assertEqual(edited.artist, post_data['artist'])
        self.assertEqual(edited.year, post_data['year'])
        
    def test_view_delete(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Test to make sure that this specific album gets deleted
    
    def test_view_read(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Make sure this single record is getting passed via context
        
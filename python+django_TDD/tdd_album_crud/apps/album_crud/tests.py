from django.test import TestCase, Client

class AlbumTest(TestCase):

    def test_hello(self):
        print("I am in Django!")

    def test_urls(self):
        c = Client()
        res = c.get('/')
        print(res)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(c.get('/add').status_code, 200)
        self.assertEqual(c.get('/delete').status_code, 200)
        self.assertEqual(c.get('/edit').status_code, 200)
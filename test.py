from unittest import TestCase
from app import app

class Forex(TestCase):


    def test_home(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/convert">', html)

    def test_convert(self):
        with app.test_client() as client:
            resp = client.get("/convert?valFrom=USD&valTo=USD&valAmount=1")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Converted Value:', html)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('$1', html)

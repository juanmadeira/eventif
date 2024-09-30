from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, response.status_code)

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsesd(response, 'index.html')
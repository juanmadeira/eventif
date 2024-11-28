from django.test import TestCase
from django.core import mail
from contact.forms import ContactForm

class ContactGet(TestCase): 
    def setUp(self):
        self.resp = self.client.get('/contact/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/contact_form.html')
    
    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 5),
            ('<textarea', 1),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
    
    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Juan Madeira",
                    email="21133654+juanmadeira@users.noreply.github.com",
                    phone="53-12345-6789", 
                    message="Mensagem teste")
        self.resp = self.client.post('/contact/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))

class ContactPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contact/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/contact_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)
    
    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class ContactSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name="Juan Madeira",
                    email="21133654+juanmadeira@users.noreply.github.com",
                    phone="53-12345-6789", 
                    message="Mensagem teste")
        resp = self.client.post('/contact/', data, follow=True)
        self.assertContains(resp, 'Mensagem enviada com sucesso!')
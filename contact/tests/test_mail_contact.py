from django.test import TestCase
from django.core import mail

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Juan Madeira",
                    email="21133654+juanmadeira@users.noreply.github.com",
                    phone="53-12345-6789", 
                    message="Boa noite, como me inscrevo?")
        self.client.post('/contact/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = "Mensagem enviada!"
        self.assertEqual(expect, self.email.subject)
    
    def test_contact_email_from(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ["contato@eventif.com.br", "21133654+juanmadeira@users.noreply.github.com"]
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'Juan Madeira',
            '21133654+juanmadeira@users.noreply.github.com',
            '53-12345-6789',
            'Boa noite, como me inscrevo?'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
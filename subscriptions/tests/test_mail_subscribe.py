from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Juan Madeira",
                    cpf='12345678901',
                    email='21133654+juanmadeira@users.noreply.github.com',
                    phone='53-12345-6789')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição!'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', '21133654+juanmadeira@users.noreply.github.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Juan Madeira',
            '12345678901',
            '21133654+juanmadeira@users.noreply.github.com',
            '53-12345-6789'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
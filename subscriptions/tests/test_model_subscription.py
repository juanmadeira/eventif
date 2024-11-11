from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name = "Juan Madeira"
                cpf = "12345678901",
                email = "21133654+juanmadeira@users.noreply.github.com",
                phone = "53-12345-6789"
            )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exist())

    def test_created_at(self):
        self.assertIsInstace(self.obj.created_at, datetime)
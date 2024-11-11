from django.test import TestCase

class SubscriptionModelTest(TestCase):
    def test_create(self):
        obj = Subscription(
            name = "Juan Madeira"
            cpf = "12345678901",
            email = "21133654+juanmadeira@users.noreply.github.com",
            phone = "53-12345-6789"
        )
        obj.save()
from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuItemTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        item = Menu.objects.get(title='IceCream')
        self.assertEqual(str(item), "IceCream : 80.00")
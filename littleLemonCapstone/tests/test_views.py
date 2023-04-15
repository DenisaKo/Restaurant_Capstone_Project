from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User

from Restaurant.models import Menu, Booking
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=100, inventory=10)
        User.objects.create_user(username='den', password='abcdef', email='den@gmail.com')
        

    def test_getall(self):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        url = reverse('menu_item_view')
        self.client.login(username='den', password='abcdef')
        response = self.client.get(url, format='json')

        self.assertEqual(serializer.data, response.data)

        
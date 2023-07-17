from django.test import TestCase 
from django.urls import reverse 
from ..models import Menu 
import json 

class MenuViewTest(TestCase): 
    def setUp(self): 
        Menu.objects.create(title="Pizza", price=12, inventory=50) 
        Menu.objects.create(title="Burger", price=8, inventory=100)
        Menu.objects.create(title="Salad", price=6, inventory=30) 

    def test_getall(self): 
        response = self.client.get(reverse('menu-list'))
        data = [{"id": 1, "title": "Pizza", "price": "12.00", "inventory": 50},
                {"id": 2, "title": "Burger", "price": "8.00", "inventory": 100},
                {"id": 3, "title": "Salad", "price": "6.00", "inventory": 30}
                ]
        self.assertEqual(json.loads(response.content.decode('utf-8')), data)
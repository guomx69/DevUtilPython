import unittest
from shopping_list import ShoppingList

class ShoppingListTest(unittest.TestCase):
    def test_add_item(self):
        shopping_list = ShoppingList()
        shopping_list.add_item("1234ABCD","Milk",1.50,1)
        self.assertEqual(shopping_list.items,
                         [{"id":"1234ABCD","name":"Milk","price":1.50,"quantity":1}]   ) 

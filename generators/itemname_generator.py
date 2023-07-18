import random

class ItemDataGenerate:
    def __init__(self):
        self.item_types = {
            "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }

    def generate_itemdata(self):
        item_type = list(self.item_types.keys())
        item_type = random.choice(item_type)

        item_names = list(self.item_types[item_type])
        item_name = random.choice(item_names)

        item_price = self.item_types[item_type][item_name]
        
        
        # print(item_type, item_name, item_price)
        return f'{item_name+item_type},{item_type},{item_price}'

# a = ItemDataGenerate()
# a.generate_itemdata()

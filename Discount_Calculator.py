class Item:

    def __init__(self,  price: float,off_percent: float, quantity=1):

        # Assign to self object
        self.price = price
        self.quantity = quantity
        self.off_percent = off_percent

    # def calculate_total_price(self):
    #     return self.price * self.quantity

    def apply_discount(self):
        after_discount = (self.price * (100 - self.off_percent))/100
        print(after_discount)
        return after_discount
        # return (after_discount)

    def __repr__(self):
        return self.apply_discount()

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)
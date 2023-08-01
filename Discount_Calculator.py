class Item:

    def __init__(self,  price: float,off_percent: float, quantity=1):

        # Assign to self object
        self.price = price
        self.quantity = quantity
        self.off_percent = off_percent

    def calculate_total_price(self):
        Org_price = self.price * self.quantity
        return Org_price 

    def apply_discount(self):
        after_discount = ((self.price * (100 - self.off_percent))/100) * self.quantity
        return float(after_discount)
        # return (after_discount)

    def __repr__(self):
        # dis_price = self.apply_discount()
        return f"The orginal price was {self.calculate_total_price()} you got it for {self.apply_discount()}"

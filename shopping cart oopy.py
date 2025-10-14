class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):

      for item in self.items:
          if item[0] == item_name:
              self.items.remove(item)
              break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
#driver Code
Cart = ShoppingCart()
#Add items to the Shopping Cart
Cart.add_item("Apple",100)
Cart.add_item("Guava",200)
Cart.add_item("Orange",150)

print("Current Items in Cart:")
for item in Cart.items:
    print(item[0],"_", item[1])

total_qty = Cart.calculate_total()
print("Total quantity:",total_qty)

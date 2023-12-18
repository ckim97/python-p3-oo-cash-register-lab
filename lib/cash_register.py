#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, multiplier=1):
    self.total += price * multiplier
    for _ in range(multiplier):
            self.items.append(item)
    self.previous_transactions.append(
          {"item": item, "multiplier": multiplier, "price": price}
        )
  
  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
        

  def void_last_transaction(self):
    if self.previous_transactions:
      last_transaction = self.previous_transactions[-1]

      price = last_transaction["price"]
      self.total -= price

      item = last_transaction["item"]
      multiplier = last_transaction["multiplier"]

      for i in range(multiplier):
         self.items.remove(item)
      
      if len(self.items) == 0:
         self.total = 0.0
      
      self.previous_transactions.pop()

c = CashRegister(10)
c.add_item("tomato", 1.76, 2)
print(c.total)
print(c.items)
c.apply_discount()
c.void_last_transaction()
print(c.total)
print(c.items)
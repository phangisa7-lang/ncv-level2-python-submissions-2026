def place_order(item):
    print(f"order placed: your order is {item}")
#eggs => 4
    #tot = (base_price + 5) * 1.15
def calculate_total(item):
    base_price = 25.5
    VAT = 0.15
    totalPrice = (base_price + len(item)) * 1.15
    return totalPrice
    
def get_order():
    print("preparing order ...")
    return "Collect Your Order"

myFood = input("What would you like? ")

place_order(myFood)

print(get_order())
order_total = calculate_total(myFood)
print(f"Your order costs: R{round(order_total,2)}")

# *args sao varios argumentos
# **kwargs sao keyword arguments, ou seja sao argumentos que tenho que passar um nome.....

def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("\nDetails of the order are:")
    for key, value in details.items():
        print(f"- {key}: {value}")

order_pizza("large", "pepperoni", "olives", delivery=True, tip=5)


nums = [2, 5, 7, 1, 9]
print(nums)
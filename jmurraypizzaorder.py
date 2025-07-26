priceSlice = 0.55

priceEaTopping = 1.25

pizzaAreaConst = 3.1414

taxRate1 = 8.5

taxRate2 = 5.0

radiusConst = 1.15

pizzaSize = int(input("Enter pizza size "))

if pizzaSize not in (1, 2, 3):
    pizzaSize = 1

pizzaRadius = pizzaSize * radiusConst

pizzaArea = pizzaAreaConst * (pizzaRadius **2)

numToppings = int(input("Enter the number of toppings "))

if numToppings < 0 or numToppings > 8:
    numToppings = 1

pizzaQuantity = int(input("Enter quantity "))

if pizzaQuantity < 0:
    pizzaQuantity = 1
elif pizzaQuantity > 50:
    pizzaQuantity = 50


pizzaAreaPrice = pizzaArea * priceSlice * pizzaQuantity

toppingsPrice = numToppings * priceEaTopping * pizzaQuantity

grossPizzaPrice = pizzaAreaPrice + toppingsPrice

salesTaxRate = taxRate1 if grossPizzaPrice > 100 else taxRate2

totalPrice = grossPizzaPrice + (grossPizzaPrice * salesTaxRate/ 100)

print(f"Pizza Size: ${pizzaAreaPrice:.2f}")

print(f"Toppings: ${toppingsPrice:.2f}")

print(f"Gross Sale Price: ${grossPizzaPrice:.2f}")

print(f"Tax: {grossPizzaPrice * salesTaxRate / 100:.2f}")

print(f"Pizza Total: {totalPrice:.2f}")























   








               

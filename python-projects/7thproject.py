foods=[]
prices=[]
total=0

while True:
    food=input("what do you wanna buy and enter q if you dont want to :")
    if food == 'q' or food == 'Q':
        break
    else:
        price=float(input(f"enter the price of {food}:   "))
        foods.append(food)
        prices.append(price)
        
print("----your orders----")

for i in foods:
    print(i, end=" ")

for i in prices:
    total+=i
    print()
    print(f"total is:{total}")

    
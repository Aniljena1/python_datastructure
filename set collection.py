CarPrices=eval(input("Enter car prices:"))
discountset=set()
for i in CarPrices:
    discount=i*(20/100)
    discountset.add(discount)
print("discount set=",discountset)

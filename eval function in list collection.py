Tvprices=eval(input("Enter tv prices:"))
print("all tv prices=",Tvprices)
for i in Tvprices:
    Discount=i*(10/100)
    print("Tv price=",i-Discount)

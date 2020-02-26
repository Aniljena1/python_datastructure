BookPrices=eval(input("Accept Book prices from the set:"))
ResultSet=set()
for i in BookPrices:
    StateGST=i*(2/100)
    CentralGST=i*(4/100)
    TotalTask=StateGST+CentralGST
    Discount=i*(2/100)
    i=(i+TotalTask)-Discount
    ResultSet.add(i)
ResultList=list(ResultSet)
print(ResultSet)
print(type(ResultSet))
ResultTuple=tuple(ResultSet)
print(type(ResultSet))

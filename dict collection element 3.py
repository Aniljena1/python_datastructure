SmartPhoneModules=eval(input("Enter smart modules in the form of list:"))
SmartPhonePrice=eval(input("Enter smart phone price in the form of list:"))
SmartPhoneDictionary={}
for i in range(0,4):
    SmartPhoneDictionary[SmartPhoneModules[i]]=SmartPhonePrice[i]
print("*"*30)
print(" SMARTPHONE MODULES   SMARTPHONE PRICE ")
print("*"*30)
for i in SmartPhoneDictionary:
    print(i,'                    ',SmartPhoneDictionary[i])
    

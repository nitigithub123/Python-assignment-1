s=int(input("enter gross income:"))
sd=10000
nod=int(input("enter number of dependents"))
ad= nod*3000
taxable_amount= s-sd-ad
tax=(20/100)*taxable_amount
print("tax is",tax)

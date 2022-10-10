totalBill=float(input("What is the total Bill? "))
numberOfPeople=int(input("Enter the Number of People "))
tipPercentage=int(input("What is the tip amout you want to give to '10' or '12' or '15' perncentage \n"))

eachpersonamount=(totalBill/numberOfPeople)
tip=1+(tipPercentage/100)
eachpersonamountaftertip=round(eachpersonamount*tip,2)
print(f"Each person should pay {eachpersonamountaftertip} amount ")

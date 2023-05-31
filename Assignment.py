
Fixed_Amount = int(input("Enter the Fixed Deposit ammount: "))
Gender = input("Enter your gender (Male = 1 and Female = 0: )")
Status = input("Are you senior Citizen (Yes = 1 and No = 0: )")

if (Gender==0) and (Status==1):
    Interest = Fixed_Amount * 8/100
    print("Your Interest is ",Interest)

elif (Gender==0) and (Status==0):
    Interest = Fixed_Amount * 6/10010
    print("Your Interest is ",Interest)

elif (Gender==1) and (Status==1):
    Interest = Fixed_Amount * 7/100
    print("Your Interest is ",Interest)
    
elif (Gender==1) and (Status==0):
    Interest = Fixed_Amount * 5/100
    print("Your Interest is ",Interest)
else:
    print("Please check your inputs!!!")


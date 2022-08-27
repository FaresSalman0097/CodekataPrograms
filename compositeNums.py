num=int(input("Enter the number : "))
if (num>3):
    for i in range (2,num):
        if (num%2==0 or num%3==0 or num%7==0 ):
            print("The number is a composite number")
            break
        else:
            print("The number is not a composite number")
            break
else:
    print("The number is not a composite number")
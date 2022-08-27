s=input("Enter the string : ")
s=s.lower()
length=len(s)
rvrsd=""
i=length-1
while(i>=0):
    rvrsd=rvrsd+s[i]
    i=i-1
print(rvrsd)
if(s==rvrsd):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

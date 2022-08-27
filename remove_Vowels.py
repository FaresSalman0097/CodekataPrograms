'''You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1
Input Description:
You are given a string ‘s’.
Output Description:
Print only consonants.
Sample Input :
I am shrey
Sample Output :
 m shry'''
s=input("Enter the string : ")
s=s.lower()
print(len(s))
for i in range(len(s)) :
    if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        continue
    else:
        print(s[i],end="")
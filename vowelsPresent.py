'''Given a string S, print 'yes' if it has a vowel in it else print 'no'.
Sample Testcase :
INPUT
codekata
OUTPUT
yes'''
s=input("Enter a string")
s=s.lower()
length = len(s)
for i in range(length):
    ch=s[i]
    if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("yes")

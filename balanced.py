s=input()
length = len(s)
if length%2==0:
    i=0
    while (i<length/2):
        j = length - 1
        while (j > 0):
            print(s[j])
            j = j - 1
            print(s[i])
            if (s[i] == s[j]):
                print(1)
            else:
                print(0)
        i=i+1

else:
    print(0)
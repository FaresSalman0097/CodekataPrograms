Num=input()
evn = [i for i in Num if int(i)%2==0]
odd = [i for i in Num if int(i)%2!=0]
evn.sort()
odd.sort()
print(*evn)
print(*odd)
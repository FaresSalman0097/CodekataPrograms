n=int(input("Enter the number of months : "))
initial_Saving=1000
mnthly_saving=1000
for i in range(1,n+1):
    mnthly_saving = initial_Saving + mnthly_saving
    initial_Saving=mnthly_saving
print(mnthly_saving)
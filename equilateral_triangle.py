import math

side=float(input("Enter the side : "))

#Area
area = round((math.sqrt(3)/4)*(side**2),2)
print("The Area of equilateral triangle is : ",area)

#Perimeter
perimeter = 3*side
print("The Perimeter of equilateral triangle is : ",perimeter)

#semi perimeter
semi_Perimeter = perimeter/2
print("The Semi perimeter of equilateral triangle is : ",semi_Perimeter)

#Altitude
altitude = (math.sqrt(3)/2)*side
print("The Altitude of equilateral triangle is : ",altitude)

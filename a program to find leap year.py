year= int(input("Enter an year"))
result= "Leap Year" if year%400 == 0 else "Leap Year" if year%4 == 0 and year%100!= 0 else "not leap year"
print(result)

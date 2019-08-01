print("**************************************")
a= int(input("student Id"))
b= (input("Student Name"))
print("Enter the subject below")
c= int(input("Hindi:"))
d= int(input("English:"))
e= int(input("SST:"))
f= int(input("Sanskrit:"))
h= c+d+e+f
i= float()
i= h/400*100
round(i)
print(i)
print(round(i))
if (i<33):
    print("you are fail")
elif(round(i)>33<50):
    print("3rd division")
elif(i>49<65):
    print("2nd division")
else:
    (i>65<100)
    print("1st division")
print("***************************************")

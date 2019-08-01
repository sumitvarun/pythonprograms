name=input("Enter Your Name")#take input from user
f= open("info.txt","w")#create file
f.write("Customer name : ")#print "customer name" in file info.txt
f.write(name)#print name variable from user
f.close()


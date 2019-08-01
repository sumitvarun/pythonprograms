class school:
    def __init__(self):    
        print("Hello Python")
        id=int(input('ENter Id:'))
        Name=input("Enter name")
        mobile=input("Enter mobile")
        #self.studentinfo(1,"Sumit",'96868596')
        self.studentinfo(id,Name,mobile)
    def studentinfo(self,id,Name,Mobile):
        print("id      :\t",id)
        print("Name    :\t",Name)
        print("Mobile  :\t",Mobile)
        self.student()
    def student(self):
        print(" I am a student of python")

r=school()
#r.studentinfo(1, "Sumit","96868596")
    

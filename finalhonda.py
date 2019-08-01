#Cars selection

class Maruti:  #class1 created 
    
    #this is a constructor and it will call automatically once instance has been created
    def __init__ (self):
        print("1. Alto")
        print("2. swift")
        print("3. WagnoR")
        print("4. Ritz")
        choice=int(input('Enter your choice: '))# integer value enter by user.
        if(choice==1):
            self.Alto()
        if(choice==2):
            self.Swift()
        if(choice==3):
            self.Wagnor()
        if(choice==1):
            self.Ritz()
    
    def Alto(self):#this is a function call by constructor
        print("******************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                         :",Price       )
        print("Mileage                       :",Mileage     )
        print("Engine                        :",Engine      )
        print("Transmission                  :",Transmission)
        print("******************************************************")
        
    def Swift(self):
        print("*****************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                        :",Price        )
        print("Mileage                      :",Mileage      )
        print("Engine                       :",Engine       )
        print("Transmission                 :",Transmission )
        print("*****************************************************")
        
    def Wagnor(self):
        print("*****************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                        :",Price        )
        print("Mileage                      :",Mileage      )
        print("Engine                       :",Engine       )
        print("Transmission                 :",Transmission )
        print("*****************************************************")
        
    def Ritz(self):
        print("***************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price       :",Price)
        print("Mileage     :",Mileage)
        print("Engine      :",Engine)
        print("Transmission:",Transmission)
        print("***************************")
class Hyundai:  #class2 created
    #this is a constructor and it will call automatically once instance has been created
    def __init__ (self):
        print("1. Verna")
        print("2. Santro")
        print("3. Creta")
        print("4. Grand")
        choice=int(input('Enter your choice: '))
        if(choice==1):
            self.Verna()
        if(choice==2):
            self.Santro()
        if(choice==3):
            self.Creta()
        if(choice==1):
            self.Grand()

            
            
    def Verna(self):    #function created

        print("*****************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                    :",Price           )
        print("Mileage                  :",Mileage         )
        print("Engine                   :",Engine          )
        print("Transmission             :",Transmission    )
        print("****************************************************")
        
    def Santro(self):
        print("************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                   :",Price           )
        print("Mileage                 :",Mileage         )
        print("Engine                  :",Engine          )
        print("Transmission            :",Transmission    )
        print("************************************************")
        
    def Creta(self):
        print("**************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                              :",Price       )
        print("Mileage                            :",Mileage     )
        print("Engine                             :",Engine      )
        print("Transmission                       :",Transmission)
        print("***************************************************")
        
    def Grand(self):
        print("*************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                    :",Price        )
        print("Mileage                  :",Mileage      )
        print("Engine                   :",Engine       )
        print("Transmission             :",Transmission )
        print("************************************************")
        
class Honda:  #This is class3.
    
    #this is a constructor and it will call automatically once instance has been created
    def __init__ (self):
        
        print("1. Civic")
        print("2. Accord")
        print("3. City")
        print("4. CRV")
        choice=int(input('Enter your choice: '))#value take by user
        if(choice==1):
            self.Civic()
        if(choice==2):
            self.Accord()
        if(choice==3):
            self.City()
        if(choice==4):
            self.CRV()

    def Civic(self):
        print("************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                     :",Price         )
        print("Mileage                   :",Mileage       )
        print("Engine                    :",Engine        )
        print("Transmission              :",Transmission  )
        print("*************************************************")
        
    def Accord(self):
        print("*************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("Price                    :",Price        )
        print("Mileage                  :",Mileage      )
        print("Engine                   :",Engine       )
        print("Transmission             :",Transmission )
        print("************************************************")
        
    def City(self):
        print("************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("|Price                    :",Price           )
        print("|Mileage                  :",Mileage         )
        print("|Engine                   :",Engine          )
        print("|Transmission             :",Transmission    )
        print("************************************************")
        
    def CRV(self):
        print("**************************************************")
        Price= "INR. 4,50,000"
        Mileage= "876876"
        Engine= "jhkjh"
        Transmission="automatic"
        print("|Price                            :",Price        )
        print("|Mileage                          :",Mileage      )
        print("|Engine                           :",Engine       )
        print("|Transmission                     :",Transmission )
        print("***************************************************")

##r=Hyundai()
##r=Honda()

print("**********************************************")
print("|              1. maruti                     |")
print("|              2. hundai                     |")
print("|              3. honda                      |")
print("**********************************************")
b=int(input("enter company number"))#value take by user
if(b==1):
    m=Maruti()
if(b==2):
    n=Hyundai()
if(b==3):
    b=Honda()
else:
    print("error")

                 
        
        
        
        
        

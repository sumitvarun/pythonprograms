class Maruti:
    def __init__(self):
        print("Maruti")
        Maruti=(input("Enter car:"))
        Model=int(input("Enter Model:"))
        Year=int(input("Enter Year:"))
        self.Marutiinfo(Model)
    def Marutiinfo(self,Model):
        print("Model no   :\t",Model)
        self.Info(Year)
    def Info(self):
        print("Year no     :\t",Year)
r=Maruti()
r.Marutiinfo()
r.Info()
        
    
        

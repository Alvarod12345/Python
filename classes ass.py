# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:53:14 2019

@author: Ankur Singh
"""

"""
Python is easy : Homework assignment #9
Classes
"""

# creating a class
class Vehicle:
    def __init__(self, make, model, year, wt, TSM, NM):           #declaring class attributes
        self.make = make
        self.model = model
        self.year = year
        self.weight =wt
        self.TripsSinceMaintenance = TSM
        self.NeedsMaintenance = NM
        
    def getMake(self):                          #getter
        return self.make                        #function used to get the value
    
    def setMake(self, make):                    #setter
        self.make = make                        #function used to set the value
        
    def getModel(self):
        return self.model
    
    def setModel(self):
        self.model = model
        
    def getYear(self):
        return self.year
    
    def setYear(self):
        self.year = year
        
    def getWeight(self):
        return self.weight
    
    def setWeight(self,wt):
        self.weight = wt
    
            
Vhcl = Vehicle("make", "model", "year", "wt", 0, False)
        

#child class is created which will inherit the properties of their parent class     
class Cars(Vehicle):                                               
    def __init__(self, make, model, year, wt, TSM, NM, isDriving):
        Vehicle.__init__(self, make, model, year, wt,TSM, NM)
        self.isdriving = isDriving
        
    def Drive(self):
        self.isDriving = True
        
    def Stop(self):
        self.isDriving = False
        
    def Repair(self):    
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False
    
    def Switching(self):
        if self.isDriving == True:
            self.TripsSinceMaintenance = 0
        else:
            self.TripsSinceMaintenance = self.TripsSinceMaintenance + 1
            if self.TripsSinceMaintenance > 100:
                    self.NM = True
                
car1 = Cars("Lamborghini", "Huracan", 2018, 1450, 0, False, True)
car2 = Cars("Aston Martin", "DB11", 2017, 1800, 150, True, False)
car3 = Cars("Ferrari", "GTC4Lusso", 2016, 1700, 70, False, False)
    
car1.Drive()
car1.Stop()
car1.Drive()
car1.Drive()
car1.Stop()
car1.Switching()

car2.Drive()
car2.Stop()
car2.Drive()
car2.Drive()
car2.Stop()
car2.Switching()

car3.Drive()
car3.Stop()
car3.Drive()
car3.Drive()
car3.Stop()
car3.Switching()

car1.Repair()
        
print("Make                  : "+car1.make)
print("Model                 : "+car1.model)
print("Year                  : "+str(car1.year))
print("Weight                : "+str(car1.weight))
print("TripsSinceMaintenance : "+str(car1.TripsSinceMaintenance))
print("NeedsMaintenance      : "+str(car1.NeedsMaintenance)+"\n")

print("Make                  : "+car2.make)
print("Model                 : "+car2.model)
print("Year                  : "+str(car2.year))
print("Weight                : "+str(car2.weight))
print("TripsSinceMaintenance : "+str(car2.TripsSinceMaintenance))
print("NeedsMaintenance      : "+str(car2.NeedsMaintenance)+"\n")

print("Make                  : "+car3.make)
print("Model                 : "+car3.model)
print("Year                  : "+str(car3.year))
print("Weight                : "+str(car3.weight))
print("TripsSinceMaintenance : "+str(car3.TripsSinceMaintenance))
print("NeedsMaintenance      : "+str(car3.NeedsMaintenance)+"\n")    
            
    
        
    
        
        
        
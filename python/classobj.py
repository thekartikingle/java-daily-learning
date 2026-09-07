# class Employee :

#     def __init__(self,salary,name,bond):                     
#         self.salary=salary
#         self.bond=bond
#         self.name=name

#     def showsalary(self):
#         return self.salary
    
#     def showinfo(self):
#         print(f"My name is {self.name}.I earn {self.salary}. I will be here for {self.bond}.")
    

# e=Employee(100000,"kartik",5)   #object of class
# print(e.showsalary()) 
# print(e.showinfo()) 

#INHERITANCE

class Animal:
    def __init__ (self,name):
        self.name=name

    def speak(self):
        print("woof")

a=Animal("dog")
a.speak()

class Dogg(Animal):
    def speak(self):
        print("bhauuu")

d=Dogg("goli")
d.speak()
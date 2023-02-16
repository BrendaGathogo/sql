class Person:
     def __init__(self,name,age):
         self.name= name
         self.age= age
     def say_hello(self):
         print(f"Hello, my name is {self.name} and my age is {self.age}")
#creating my object
person1=Person("Brenda",18)
person1.say_hello()
person2=Person("Mercy",20)
person2.say_hello()
person3=Person("Remii",19)
person3.say_hello()
#create a class called cars with the folowing attriutes/properties
#make,model,year them create a function that prints make,model and year
#then create three objects
class Cars:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def  say_this(self):
        print(f"This car is a {self.make},of model {self.model} ,and made in the year {self.year}")
car1=Cars("chevrolet","suv",2020)
car1.say_this()
car2=Cars("Lexus","lexus IS 350",2021)
car2.say_this()
car3=Cars("Lincoln","Towncar",2022)
car3.say_this()
class Clothes:
    def __init__(self,brand,type,price):
        self.brand= brand
        self.type= type
        self.price= price
    def say_the(self):
        print(f"The description of the clothing is {self.brand} ,{self.type},{self.price}")
c1=Clothes("LCWaikiki","shirt",2000)
c1.say_the()
c2=Clothes("mrp","trouser",2500)
c2.say_the()
c3=Clothes("Woolworth","dress",5000)
c3.say_the()
c4=Clothes("citywalk","shoes",3000)
c4.say_the()
#example4
class Schools:
    def __init__(self,name,location,principle):
        self.name=name
        self.location=location
        self.principle=principle
    def say_the(self):
        print(f"The name of the school is {self.name},we are located in {self.location} and the principle is {self.principle}")
s1=Schools("Kirawa","Kitusuru","Mr.Ireri")
s1.say_the()
s2=Schools("Potterhouse","Runda","Mr.Ivan")
s2.say_the()
s3=Schools("Montessori","Westlands","Mrs.Yvette")
s3.say_the()
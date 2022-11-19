# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
# It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self,name, age, coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    def description(self):
        print(f"name of the Dog is {self.name}")
        print(f"age of the dog is {self.age}")
        
    def get_info(self):
        print(f'coat color of the dog is {self.coat_color}')
        
class JackRussellTerrier(Dog):
    def __init__(self,name, age, coat_color,hieght="25-38 cm",mass="6-8 kg",bodylength="46-55cm"):
        super().__init__(name, age, coat_color)
        self.hieght=hieght
        self.mass=mass
        self.bodylength=bodylength
    def lifespan(self,lifeline="Lifespan of this dog breed is 12-16 years"):
        print(lifeline)
        
    def temprament(self):
        temper="Temprament of this dog breed is Intelligent, Stubbon, Athletic, Energetic, Fearless"
        print(temper)
        
    def getappearance(self):
        print(f"height of Jack Russell Terrier is {self.hieght}")
        print(f"weight of Jack Russell Terrier is {self.mass}")
        print(f"overall bodylength of Jack Russell  Terrier is {self.bodylength}")
         

class Bulldog(Dog):
    def __init__(self,name, age, coat_color,hieght="31-40 cm",mass="23-25 kg",bodylength="51-69 cm"):
        super().__init__(name, age, coat_color)
        self.hieght=hieght
        self.mass=mass
        self.bodylength=bodylength
        
    def lifespan(self):
        lifeline="Lifespan of this dog breed is 8-10 years"
        print(lifeline)
        
    def temprament(self):
        temper="Temprament of this dog breed is Docile, Friendly, Gregacious"
        print(temper)
        
    def getappearance(self):
        print(f"height of Bulldog is {self.hieght}")
        print(f"weight of Bulldog is {self.mass}")
        print(f"overall bodylength of Bulldog is {self.bodylength}")
        

J=JackRussellTerrier("Jackson",5,"White")
J.description()
J.get_info()
J.getappearance()
J.temprament()

B=Bulldog("Heather", 7, "Brindle & White")
B.description()
B.get_info()
B.getappearance()
B.temprament()
class Pet:
    name = str
    species = str
    age = int

    def __init__(self,name, species, age):
        self.name = name
        self.species = species
        self.age =age
        
    def display_info(self):
        print(self.name)
        print(self.species)
        print(self.age)
        

    def is_eligible_for_adoption(self):
        if self.age < 10:
            return True
        else:
            return False
    
pet1 = Pet('Tommy', 'Dog', 11)

pet1.display_info()
print(pet1.is_eligible_for_adoption())

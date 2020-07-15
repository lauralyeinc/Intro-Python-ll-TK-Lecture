class Human: 
    def __init__(self, name, pets=None):
        self.name = name
        if pets is None:
            self.pets = []
        else:
            self.pets = pets
        # or
        # self.pets = pets
        # if self.pets is None:
        #     self.pets= []
    def add_pet(self,  new_pet):
        self.pets.append(new_pet)
        new_pet.owners = self 

# related to the abstraction is_a has_a dog is an animal, animal has_an owner. 

class Animal:
    count = 0  # class attritube 
    def __init__ (self, name, color, height, diet, species, owners=None):
        #attrbutes / parameters 
        self.name = name
        self.color = color
        self.height = height
        self.diet = diet
        self. species = species
        self.owners = owners 
        Animal.count += 1  
    #actions 
    def speak(self):
        # would take to long to code for each animal. not really making a print anymore. It's not abstraction shell to add information  
        # if self.species == "DOG":
        #     print("woof")
        # elif self.species == "BIRD":
        #     print("tweet")
        # elif self.species == " CAT":
        #     print("meow")
        # else:
        #     print("I don't know if I made a sound.")
        pass
    def eat(self, food):
        pass # pass means:skip. and reads it without an whitespace error. 
    def sleep(self):
        print("zzzzzz")

    # @abstractmethod  #<--- You can't make a relational animal to the animal class with the move action. You have to build something like the Dog class first and it overrides that abstract method. 
    def move(self):
        pass

class Dog(Animal):
    def __init__ (self, name, color, height, owners=None):  #<-- passed only  because a new dog could be black or purple or have a different name.  It's still a blank card for a dog from the animal class.. they will always be a dog and a carnivore.
        super().__init__(name, color, height,"CARNIVORE", "DOG", owners) #<--- inherts from the parent class of Animal could use Animal.__init__ as well to be more clear, super is conventional. 
        self.owners= owners # another type class  many to one owner has many pets, pet is owned by one owner. 
    def speak(self):
        print("woof")
    def eat(self, food):
        if food == "MEAT":
            print("Yum")
        else:
            print("yuck")
    def move(self):
        print(f'{self.name} walks.')


dog = Dog("Alllie", "Brown", 24)
dogo = Dog("Yeller", "Yellow", 40)
print(dog.species)  # DOG √√ 
print(dog.sleep()) # zzzz √√ 

#random print of None here.... 

myself = Human("Laura")
print(myself.name) #√√ Laura 

print(Animal.count) # √√ two dogs in the animal class. 


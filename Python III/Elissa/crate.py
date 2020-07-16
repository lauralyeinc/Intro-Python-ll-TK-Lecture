from product import Product

class Crate(Product):
    def __init__(self, name, description, price, size, material):
        # self.name = name
        # self.description = description
        # self.price = price
            #constructor go run the function in the parent function
        super().__init__(name, description, price)
        # unqiue attrs to the crate object/class
        self.size = size
        self.material = material
    
    def __str__(self):
        # return f' {self.name} is ${self.price} and it is made of {self.material}.'
        return super().__str__() + f' and is made of {self.material}.'

c = Crate("GreatCrate", "descrip", 79, "small", "metal")
print(c)

print(super(Crate, c).__str__())
# this prints the parent class __str__ GreatCrate is $79 and not the Crate __str__  can refer to any of the parent methods. 


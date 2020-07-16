class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products # also an abstract set up to set up a formal [] of products later. 
    def __str__(self):
        return f' {self.name} : {self.description}'
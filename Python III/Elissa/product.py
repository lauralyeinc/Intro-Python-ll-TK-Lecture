class Product:
    def __init__(self, name, description, category, price=0):
        self.name = name
        self.description = description
        self.category = category
        self.price = price 


    def __str__(self):
        return f'{self.name} : ${self.price}'
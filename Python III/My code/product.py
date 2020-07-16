class Product:
    def __init__(self, name, description, price=0):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} is ${self.price}'
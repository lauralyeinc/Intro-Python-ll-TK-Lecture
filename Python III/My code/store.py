class Store():
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories #abstract list but not formally marked [].
    
    def __str__(self):
        output = f' Hello! Welcome to {self.name}!'
        for category in self.categories:
            output += f'\n {str(category)}'
        return output

    def __repr__(self):
        return f'self.name = {self.name} ; self.categories = {self.categories}'

# create basic store with abstract categories. 
#the_store = Store("The Store", ["white wine", "chocolate", "coffee"])

#print(the_store) #√√ 

# add formal [] categories for the_store we made from the store class. 
from category import Category
# imported the blueprint class of a category
#make a few categories.
    # formally set up but only in string form. Don't have product class made yet. 
# Wine_cat = Category("Wine", "All the goodness in the world", ["White", "Rose", "Red"])
# Chocolate_cat = Category("Chocolate", "Willy Wonka would be proud.", ["Dark", "White", "Pink", "Milk"])
# Coffee_cat = Category("Coffee", "Hot Bean Water for Life!", ["Drip", "Espresso", "Latte"])

# Now adding the formal categories to REAL the_store set up.
    # the category stays in a formal list because we set it up that way above.
# the_store = Store("The Store", [Wine_cat, Chocolate_cat, Coffee_cat])
# print(the_store) #√√ 

#Now settin gup the formal class for products within a category then adding them to the_store. 

from product import Product

White_Wine =  Product("Ghostly", "So white you'll want to hang out with Casper", 23)
Rose_Wine = Product("Rose All Day", "May you enjoyr your Day!", 15)
Red_Wine = Product("RubyRed", "The classic Red you need after a long day", 25)

Wine_cat = Category("Wine", "All the goodness in the world", [White_Wine, Rose_Wine, Red_Wine])

# = Product("", "", )
# White_Coco= Product("White Creme", "Yum",   12 )
# Pink_Coco= Product("Pink Coco", "Yummy", 13)
# Milky_Way= Product("Milky Way", "it's okay", 2)
# Dark_Chocolate = Product("Dark Chococlate", "Healthiest!", 15)

# Cheap= Product("Drip", " Every day all day", 2)
# Engery= Product("Espresso", "Get that boost of energy", 5)
# Relax= Product("Latte", "Grab a book and enjoy", 6)


# now add all the classes together!!!
the_store = Store("The Store", [Wine_cat])
print(the_store)

# Chocolate_cat = Category("Chocolate", "Willy Wonka would be proud.", ["Dark", "White", "Pink", "Milk"])
# Coffee_cat = Category("Coffee", "Hot Bean Water for Life!", ["Drip", "Espresso", "Latte"])

# moved to category_a.py to learn how to keep each class in it's one file/folder set up. 
# class Category: 
#     def __init__(self, name, description, products):
#         self.name = name
#         self.description = description
#         self.products = products 
    
#     def __str__(self):
#         return f" {self.name} :  {self.description} "

# import from other places
from category_a import Category  # importing just the class Category from the category_a.py file 

class Store:
    #attributes
    # name
    # categories (departments)
    
    # construction - oop term - function that runs every time you create a new instance
    # self keyword is like this in JS. current instance of the class. 
    def __init__(self, name, categories):
        #have to assign the attritubes to the that self item. if not assigned it's just there but it's stuck in there without a return (JS logic). 
        self.name = name
        self.categories = categories
        # default attritubes
        self. employees = []

    # str transforms our instance of a store into a string, that way we can print the store object. 
    def __str__(self):
        # return a string representing the store 
        output = f"Hello. Welcome to {self.name}!"
        for cat in self.categories:
            output += f'\n {str(cat)}'
        return output


        # this returns the correct store string, welcome to storename, but it doesn't return the categories __str__ method, it's returns the object location of each category, above ^^^^ sets up the str in the store and then loops over each catergory to return it correctly. 

        # return f' \nWelcome to {self.name}! Here are the categories: {self.categories}. \n'  {self.categories}, isn't a defined type of collection, it could be a list, object or really anthing. The computer doesn't understand that we set up a class for categories here. 

    # also returns a string, matter of fact, help developers debug or understand class better, understand how your object is structured. 
    def __repr__(self):
        return f'self.name = {self.name} ; self.categories = {self.categories}'
    # returns what is the code that created that object or string of code, like what class and method is making that return in that way. 


# create a category for a store. 
running_cat = Category("Running", "All your running needs.", [])
camping_cat = Category("Camping", "All your camping needs", [])
tennis_cat = Category("Tennis", "All your tennis needs", [])
football_cat = Category("Football", "American Kind", [])


# create a store 
sports_store = Store("Gander", [camping_cat, running_cat, tennis_cat, football_cat] ) 
# sports_store = Stre("Gander", ["camping", "running", "tennis", "football"]) won't work anymore, because we set up a blueprint for a category and have to create one and then add it's name varible to the stores setup. 

#print(running_cat) # √√ 

food_store = Store("Trader's Joe", ["Dairy", "Meat", "Bakery", "Dry Goods"])



print(sports_store)  # using the acutal instance to call the sport object we created name sports_store. 
# prints object location if not having __str__ set up in the parent class of Store.  <__main__.Store object at 0x7ffaf51f9d90> 
# with __str__ added in parent class of Store. It prints out Welcome to Gander! Here are the categories: ['Camping', 'Running', 'Tennis', 'Biking']. 

# print(str(sports_store)) # calling str method, prints just the str in the class store. looks the same as above. Above is working thru the whole function class Store logic. 
# print(repr(sports_store)) # prints self.name = Gander ; self.categories = ['Camping', 'Running', 'Tennis', 'Biking']
print(food_store)
#print(food_store.name) 




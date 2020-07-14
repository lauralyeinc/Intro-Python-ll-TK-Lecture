class Store:
    #blueprint for the store
    def __init__(self, name, catergories, optional="False"):
        #attribtues 
        self.name = name
        self.catergories = catergories
        self.optional = optional
    
    def __str__(self):
        # return f'{self.name} has {len(self.catergories)} categories' 
        output = self.name
        #1. Food
        #2. Costumes
        #3. Toys 
        i = 1
        for cat in self.catergories:
            output += f'\n{i}. {cat}'
            i += 1 
        output += f'\n{i}. Quit'
        return output 

from category import Category
my_store = Store("Petapalooza", [Category("Food"), Category("Costumes"), Category("Toys")])
print(my_store)

# my_store = Store("Petapalooza", ["Food", "Costumes", "Toys"])

selection = int(input('Please select a catergory number:\n'))-1

while(selection != len(my_store.categories)):
    selection = int(input('Please select a catergory number:\n'))-1
    print(f' You selected {my_store.categories[selection]}')
    
    print(selection)

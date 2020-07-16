class Store:
    #blueprint for the store
    def __init__(self, name, catergories, products, 
    # optional="False"
    ):
        #attribtues 
        self.name = name
        self.catergories = catergories # list of Category objects 
        self.products = products
        #self.employees = employees  # could be a list of employees
        #just for an example (below)
        # self.optional = optional
    
    def __str__(self):
        # return f'{self.name} has {len(self.catergories)} categories' 
        output = {self.name}
        #1. Food
        #2. Costumes
        #3. Toys 
        i = 1
        for cat in self.catergories:
            output += f'\n{i}. {cat}'
            i += 1 
        output += f'\n{i}. Quit'
        
        return output

    # def __repr__(self):
    #     return f'{self.name} has {len(self.categories)} categories'


from category import Category
from product import Product

cat = [Category("Food"), Category("Costumes"), Category("Toys")]

my_store = Store("Petapalooza", cat, [Product("squeeky too", "desc", cat[3], 10), Product("cat food", "for eatting", cat[0], 5)]) # got stuck here. 

#print(new_store)


# my_store = Store("Petapalooza", ["Food", "Costumes", "Toys"], ["Wet food", "Dry food", "Wonder Woman", "Ball"])

selection = int(input('Please select a category number:\n'))-1

while(selection != len(my_store.categories)):
    print(f' You selected {my_store.categories[selection]}')
    for p in new_store.products:
        # if product is in category
        if p.category == my_store.categories[selection]:
            print(f' - {p}')
    selection = int(input('Please select a catergory number:\n'))-1


list1=[]
list2=[]
list3=[]

class category:

    code_c=1200

    def __init__(self,name):
        self.name=name
        self.code=category.code_c+1
        category.code_c+=1

    def display(self,list):
        self.no_of_products = len(list)
        print("\nCategory --> ",self.name)
        print("Code --> ",self.code)
        print("No. of products --> ", self.no_of_products)
        print("List of Products --> ", list)

class products():

    code_p = 57294
    dict_p={}
    i=0
    def __init__(self,name,category,price):
        self.name=name
        self.code=products.code_p+1
        products.code_p+=1
        self.price=price
        self.category=category
        products.i+=1
        products.dict_p.update({products.i : [self.name,self.code,self.category,self.price]})

        if self.category=="Sanitory_items":
            list1.append(self.name)
        elif self.category=="Stationary_items":
            list2.append(self.name)
        elif self.category=="Gadgets":
            list3.append(self.name)

cat1=category("Sanitory_items")
cat2=category("Gadgets")
cat3=category("Stationary_items")
product1=products("Toothbrush","Sanitory_items",120)
product2=products("Pencil","Stationary_items",5)
product3=products("Eraser","Stationary_items",7)
product4=products("Scale","Stationary_items",10)
product5=products("Mobile","Gadgets",10000)
product6=products("Fridge","Gadgets",15000)
product7=products("Toothpaste","Sanitory_items",100)
product8=products("Tissue","Sanitory_items",70)
product9=products("Headphones","Gadgets",899)
product10=products("Laptop","Gadgets",59999)


cat1.display(list1)
cat2.display(list2)
cat3.display(list3)
print()

print("Sort Price --> Low to High")
x=dict(sorted(products.dict_p.items(), key=lambda item: item[1][3]))
print(x)



print()
print("Sort Price --> High to Low")
y=dict(sorted(products.dict_p.items(), key=lambda item: item[1][3] ,reverse=True))

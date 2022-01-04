#Create class category
class category:

    code_c=100

    #For difine member of a category
    def __init__(self,name):
        self.name=name
        self.code=category.code_c+1
        category.code_c+=1
        self.no_of_products=0

    #diaplay member of category
    def display_category_information(self):
        print('Category Name: ',self.name)
        print('Category Code:',self.code)
        print('Number of Products:',self.no_of_products)

#create Product class
class Product:

    code_p=300

    #create member of a product
    def __init__(self,name,category,price):
        self.name=name
        self.code=Product.code_p+1
        Product.code_p+=1
        self.category=category.name
        self.price=price
        category.no_of_products+=1

    #diaplay member of a product
    def Product_Diaplay(self):
        print("Product:",self.name," ", "code:",self.code," ","category:", self.category," ","Price:", self.price)
        

#calling category object
cobj1=category('Electronic')
cobj2=category('BeautyCare')
cobj3=category('Stationary')

#calling product object
pobj1=[Product('mobile',cobj1,1500),
    Product('TV',cobj1,30000),
    Product('Laptop',cobj1,75000),
    Product('Fridge',cobj1,30000),
    Product('Shampoo',cobj2,500),
    Product('Conditioner',cobj2,750),
    Product('Pen',cobj3,10),
    Product('Book',cobj3,50),
    Product('Pencil',cobj3,5),
    Product('Eraser',cobj3,3)]

#diaplay product list
for x in pobj1:
    x.Product_Diaplay()

#diaplay category list
print("\n")
cobj1.display_category_information()
cobj2.display_category_information()
cobj3.display_category_information()

#sort product in ascending order using its price
print("\n")
print("Product Sorted in ascending order")
x=(sorted(pobj1,key=lambda x:x.price))
for i in x:
    i.Product_Diaplay()

#sort product in dedending order using its price
print("\n")
print("Product Sorted in Desending order")
x=sorted(pobj1,key=lambda x:x.price,reverse=True)
for i in x:
    i.Product_Diaplay()

#search product using product code
print("\n")
codenumber=int(input("Enter Product Code:"))
y = [x for x in pobj1 if x.code == codenumber]
for i in y:
    i.Product_Diaplay()





    '''pr1={"name1":"Mobile","code1":1,"category1":"Electronic","price1":15000}
    pr2={"name2":"Pen","code2":11,"category2":"Stationary","price2":10}
    pr3={"name":"shampoo","code":5,"category":"BeautyCare","price":500}
    pr4={"name":"Book","code":12,"category":"Stationary","price":50}
    pr5={"name":"Pencil","code":13,"category":"Stationary","price":5}
    pr6={"name":"Eraser","code":14,"category":"Stationary","price":3}
    pr7={"name":"TV","code":2,"category":"Electronic","price":25000}
    pr8={"name":"Laptop","code":3,"category":"Electronic","price":75000}
    pr9={"name":"Fridge","code":4,"category":"Electronic","price":30000}
    pr10={"name":"Conditioner","code":6,"category":"BeautyCare","price":700}
    #product1={1:"Mobile",2:"TV",3:"Laptop",4:"Fridge",5:"Shampoo",6:"Conditioner",11:"Pen",12:"Book",13:"Pencil",14:"Eraser"}
    #productcodelist=list(product1.keys())
    #print(productcodelist)
    if codenumber in list(product1.keys()):
        print("Product Found.")
    else:
        print("Product not found.")    
    pr= [Product("Mobile",1,"Electronic",15000),
              Product("TV",2,"Electronic",25000),
              Product("Laptop",3,"Electronic",75000),
              Product("Fridge",4,"Electronic",30000),
              Product("shampoo",5,"BeautyCare",500),
              Product("conditiner",6,"BeautyCare",750),
              Product("Book",12,"Stationary",50),
              Product("Pen",11,"Stationary",10),
              Product("Pencil",13,"Stationary",5),
              Product("Eraser",14,"Stationary",3)]    '''



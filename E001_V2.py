from treelib import Tree
import pandas as pd
# Create class category
class Category:
    code_c = 100

    # For difine member of a category
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.code = Category.code_c + 1
        Category.code_c += 1
        self.no_of_products = 0
        self.products = []
        self.display_name = self.name
        self.display_name1()

    # diaplay member of category
    def display_category_information(self):
        print('Category Name: ', self.name)
        print('Category Code:', self.code)
        print(self.display_name)
        print('Number of Products:', self.no_of_products)
        if self.no_of_products!=0:
             for i in self.products:
                print(i.name)

    #display category with it's parent
    def display_name1(self):
        countcategory = self
        while (countcategory.parent != None):
            self.display_name = f'{countcategory.parent.name} > {self.display_name}'
            countcategory = countcategory.parent

# create Product class
class Product:
    code_p = 300

    # create member of a product
    def __init__(self, name, category, price,stock_at_location={}):
        self.name = name
        self.code = Product.code_p + 1
        Product.code_p += 1
        self.category = category
        self.price = price
        category.no_of_products += 1
        self.stock_at_location=stock_at_location

    # diaplay member of a product
    def Product_Display(self):
        print("Product:", self.name, " ", "code:", self.code, " ", "category:", self.category, " ", "Price:",
              self.price)

def main():

    # calling category object
    Electronic = Category('Electronic')
    Vehical = Category('Vehical')
    Mobile = Category('Mobile',Electronic)
    Car=Category('Car',Vehical)
    Iphone=Category('Iphone',Mobile)

    listOfCategory=[Electronic,Vehical,Mobile,Car,Iphone]

    # calling product object
    pobj1 = [Product('Laptop',Electronic,750000),
         Product('TV',Electronic,30000),
         Product('Washing Machine',Electronic,27000),
         Product('scooty',Vehical,50000),
         Product('Activa',Vehical,90000),
         Product('Motor-cycle',Vehical,150000),
         Product('Samsung',Mobile,50000),
         Product('I-phone',Mobile,100000),
         Product('Mi',Mobile,15000),
         Product('Alto',Car,300000),
         Product('Shift',Car,500000),
         Product('Creta',Car,2500000),
         Product('iphone-10',Iphone,100000),
         Product('iphone-12',Iphone,500000),
         Product('iphone-13',Iphone,1000000)]

    # diaplay category list

    print("List of category")
    '''df=pd.DataFrame(t.__dict__ for t in listOfCategory)
    df['code']=df['code'].apply(lambda listOfCategory:listOfCategory.name)
    print(df)'''
    for x in listOfCategory:
        x.display_category_information()

    #display product list
    print("\n")
    print(("List of Products"))
    df=pd.DataFrame(t.__dict__ for t in pobj1)
    df['category']=df['category'].apply(lambda pobj1:pobj1.name)
    print(df)

    '''for x in pobj1:
        x.Product_Display()'''

    #display tree
    tree=Tree()
    tree.create_node("Product Category",0)
    for i in listOfCategory:
        tree.create_node(i.name,i.name,parent=0)
        if i.parent!=None:
            tree.move_node(i.name,i.parent.name)
        for c in i.products:
            tree.create_node(c.name,c.name,parent=i.name)
    print("\n")
    tree.show()

    pd.set_option('display.max_rows',500)
    pd.set_option('display.max_columns',500)
    pd.set_option('display.width',1000)

    # sort product in ascending order using its price
    print("\n")
    print("Product Sorted in ascending order")
    x = (sorted(pobj1, key=lambda r: r.price))
    df = pd.DataFrame(t.__dict__ for t in x)
    df['category'] = df['category'].apply(lambda x: x.name)
    print(df)
    '''for i in x:
        i.Product_Display()'''



    # sort product in dedending order using its price
    print("\n")
    print("Product Sorted in Desending order")
    x= (sorted(pobj1, key=lambda r: r.price, reverse=True))
    df=pd.DataFrame(t.__dict__ for t in x)
    df['category']=df['category'].apply(lambda x:x.name)
    print(df)
    '''for i in x1:
        i.Product_Display()'''

    # search product using product code
    print("\n")
    codenumber = int(float(input("Enter Product Code:")))
    y = [x for x in pobj1 if x.code == codenumber]
    for i in y:
        i.Product_Display()

if __name__ == '__main__':
    main()






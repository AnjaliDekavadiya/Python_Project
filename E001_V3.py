import os
from E001_V2 import Product,Category

class Location:
    code_l=1000
    def __init__(self,name):
        self.name=name
        self.code=Location.code_l+1
        Location.code_l+=1

    def diaplay1(self):
        print("Location name:",self.name,"Code:",self.code)

class Movement:
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        self.display=''

        try:
            if self.product.stock_at_location[self.from_location] >= self.quantity:
                qun = self.product.stock_at_location[self.from_location] - self.quantity
                self.product.stock_at_location.update({self.from_location: qun})
                if self.to_location in self.product.stock_at_location:
                    qun1 = self.product.stock_at_location[self.to_location] + self.quantity
                    self.product.stock_at_location.update({self.to_location: qun1})
                else:
                    self.product.stock_at_location.update({self.to_location: self.quantity})
                self.display = f'product quantity:{self.quantity}  {self.product.name} from {self.from_location.name} to {self.to_location.name}'
            else:
                #self.display=f" quantity no:{self.quantity}) of {self.product.name} not available {self.from_location.name}"
                print(f"\nMovement Failed --> {self.quantity} {self.product.name} does not exist in {self.from_location.name}")
        except Exception:
            #self.display="no loaction for that product"
            print(f"\nMovement Failed --> No {self.product.name} at {self.from_location.name}")

    @staticmethod
    def movement_by_product(product):
        flag=0
        save_path='C:/Users/anujp/Desktop/ftp/'
        for item in listofmovement:
            Movement.name=item.to_location.name
            completename=os.path.join(save_path,Movement.name+".txt")
            if item.product.name==product.name and item.display!='':
                flag=1
                print(item.display)
                file=open(completename,"a")
                file.writelines(item.display)
                file.write("\n")
        if flag==0:
            print("No movement yet..")


if __name__ == "__main__":
    rajkot=Location("Rajkot")
    jamnagar=Location("Jamnagar")
    ahemdabad=Location("Ahemdabad")
    surat=Location("Surat")

    listoflocation=[rajkot,jamnagar,ahemdabad,surat]
    for i in listoflocation:
        i.diaplay1()

    Electronic=Category("Electonic")

    mobile=Product("Mobile",Electronic,15000,{rajkot:30,jamnagar:40,surat:10})
    laptop=Product("Laptop",Electronic,75000,{rajkot:10,jamnagar:10,ahemdabad:10})
    tv=Product("Tv",Electronic,25000,{jamnagar:40,ahemdabad:40,surat:10})
    tablet=Product("Tablet",Electronic,10000,{rajkot:30,ahemdabad:90,surat:10})
    watch=Product("Watch",Electronic,5000,{rajkot:2,jamnagar:100,ahemdabad:10,surat:100})

    listofproduct=[mobile,laptop,tv,tablet,watch]

    for i in listofproduct:
        print(i.name)
        for key in i.stock_at_location:
            print(f'{key.name}-{i.stock_at_location[key]}')
        print()


    movement1=Movement(rajkot,jamnagar,mobile,20)
    movement2 = Movement(ahemdabad, surat, tv, 10)
    movement3 = Movement(jamnagar, rajkot, laptop, 5)
    movement4 = Movement(rajkot, ahemdabad, tablet, 20)
    movement5 = Movement(surat, ahemdabad, watch, 10)

    listofmovement=[movement1,movement2,movement3,movement4,movement5]

    for i in listofproduct:
        print(i.name)
        Movement.movement_by_product(i)
        print()
    print("new stock at location")
    for i in listofproduct:
        i.Product_Display()
        print("Location:",end=' ')
        for key in i.stock_at_location:
            print(f'{key.name}-{i.stock_at_location[key]}')
    print("\n")
    print("product list by location")
    for i in listoflocation:
        print(i.name)
        for p in listofproduct:
            if i in p.stock_at_location:
                print(f'{p.name}-{p.stock_at_location[i]}')
        print()

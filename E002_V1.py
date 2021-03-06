import re
from datetime import datetime,date
from E001_V2 import Product,Category
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#create customer class
class Customer:

    #define member of customer
    def __init__(self,name,email,phone,street,city,state,country,company,type):
        self.name=self.namevalid(name)
        self.email=self.emailvalid(email)
        self.phone=self.phonevalid(phone)
        self.street=street
        self.city=self.namevalid(city)
        self.state=self.namevalid(state)
        self.country=self.namevalid(country)
        self.company=company
        self.type=type

        if self.type=='contact' or self.type=='billing' or self.type=='shipping' or self.type=='company':
            self.type=type
        else:
            print("Invalid type..")

    #email validation
    def emailvalid(self,eml):
        emailre = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if re.search(emailre,eml):
            return eml
        else:
            print("Enter valid email")

    #phone number validation
    def phonevalid(self,num):
        phonere= "(0|91)?[7-9][0-9]{9}$"
        if re.search(phonere,num):
            return num
        else:
            print("Enter valid PhoneNumber")

    #name,state,country,city validation
    def namevalid(self,name_check):
        namere='^[A-Za-z]*$'
        if re.search(namere,name_check):
            return name_check
        else:
            print("Not valid")
            return False

    #diaplay customer details
    def display(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Phone:",self.phone)
        print(f"Address: {self.street}, {self.city}, {self.state}, {self.country}")
        if self.company=="":
            pass
        else:
            print("Company:",self.company.name)
        print("Type:",self.type)

        '''emailre = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phonere='(0|91)?[7-9][0-9]{9}'
        namere='([a-zA-Z]+|[a-zA-Z]+\\s[a-zA-Z]+)'
        '''

#create order class
class Order:

    number=2000

    #define member of order class
    def __init__(self,date,company,billing,shipping):
        self.number=Order.number+1
        Order.number+=1
        self.date=self.check(date)
        self.comapny=company
        self.order_lines = []
        self.total_amount=0

        if billing.type=='billing' and shipping.type=='shipping':
            self.billing=billing
            self.shipping=shipping
        else:
            print("Please check type")

    #date validation
    def check(self,date1):
        try:
            date_obj=datetime.strptime(date1,'%d %b %Y')
            if date_obj.date()<date.today():
                print("Past date is not valid")
            else:
                return date_obj
        except Exception as e:
            print(e)

    def totalamount(self):
        for i in self.order_lines:
            self.total_amount=self.total_amount+i.subtotal
        return self.total_amount

    #display order details
    def display(self):
        print("\nNumber:",self.number)
        print("Date:",self.date)
        print("Company:",self.comapny.name)
        print()
        print("Billing")
        print("---------------------------------------------")
        self.billing.display()
        print()
        print("Shipping")
        print("---------------------------------------------")
        self.shipping.display()
        print()
        print("Order Lines:")
        print("---------------------------------------------")

        temp = pd.DataFrame(i.__dict__ for i in self.order_lines)
        temp['order'] = temp['order'].apply(lambda x: x.number)
        temp['product'] = temp['product'].apply(lambda x: x.name)
        print(temp)
        print("Total amount: ", self.totalamount())

        ''' for i in self.order_lines:
                    print(i.order.number)'''
    @staticmethod
    def binary_search(list_o,low,high,ord_num):
        if high>=low:
            mid=(high+low)//2
            if str(list_o[mid].number)==ord_num:
                list_o[mid].display()
            elif str(list_o[mid].number) > ord_num:
                return Order.binary_search(list_o,low,mid-1,ord_num)
            else:
                return Order.binary_search(list_o,mid+1,high,ord_num)

        else:
            print("no such orders!")





#create orderline class
class OrderLine:

    #define member of orderline class
    def __init__(self,order,product,quantity,price=None):
        self.order=order
        self.product=product
        self.quantity=int(quantity)
        self.mrp=product.price
        if price is None:
            self.price = product.price
        else:
            self.price = price
        self.subtotal=(self.price*self.quantity)
        self.order.order_lines.append(self)
        self.order.totalamount()

    def display(self):
        print("Product:", self.product.name)
        print("MRP:",self.mrp)
        print("Quantity:",self.quantity)
        print("Price:",self.price)
        print("Total:",self.subtotal)


#main function
def main():
    Vehical=Category('Vehical')
    Electronic=Category('Electronic')
    Stationary=Category('Stationary')

    mobile=Product("Mobile",Electronic,15000)
    car=Product("Car",Vehical,800000)
    book=Product("Book",Stationary,100)
    pen=Product("Pen",Stationary,20)
    laptop=Product("Laptop",Electronic,5)

    listofproduct=[mobile,car,book,pen,laptop]

    Suzuki = Customer("Suzuki", "suzuki@gmail.com", "7854932810", "University", "Rajkot", "Gujarat", "India","", "company")
    Puma = Customer("Puma", "puma@gmail.com", "8756210144", "Astron", "Rajkot", "Gujarat", "India","", "company")
    Classmate = Customer("Classmate", "classmate@gmail.com", "8887779990", "Kalawad", "Rajkot", "Gujarat", "India", "", "company")
    Kinjal= Customer("Kinjal", "kinjal@gmail.com", "9856472310", "Narhe", "Pune", "Maharashtra", "India","", "billing")
    Mital= Customer("Mital", "mital@gmail.com", "9856472310", "T-square", "Jamnagar", "Gujarat", "India","", "shipping")
    Darshan= Customer("Darshan", "darshan@gmail.com", "7598624825", "Kalyan", "Mumbai", "Maharashtra", "India","", "shipping")
    Sheetal= Customer("Sheetal", "sheetal@gmail.com", "8964712500", "Cochin", "Ernakulam", "Kerala", "India","", "billing")
    Dvijesh= Customer("Dvijesh", "dvijesh@gmail.com", "8520069442", "Ace Ln.", "Dallas", "Texas", "USA","", "billing")
    Hardik= Customer("Hardik", "hardik@gmail.com", "9510022336", "Westchase", "Tampa", "Florida", "USA", "", "shipping")

    order1 = Order('12 jan 2023', Puma, Kinjal, Hardik)
    order1_line1 = OrderLine(order1, mobile, 3)
    order1_line2 = OrderLine(order1, book, 1)
    order1_line3 = OrderLine(order1, pen, 1)

    order2 = Order('12 jan 2023', Suzuki, Sheetal,Mital)
    order2_line1 = OrderLine(order2, laptop, 4)
    order2_line2 = OrderLine(order2, car, 1)

    order3 = Order('12 jan 2023', Classmate, Dvijesh, Darshan)
    order3_line1 = OrderLine(order3, pen, 10)

    order4 = Order('12 jan 2023', Puma, Kinjal, Mital)
    order4_line1 = OrderLine(order4, mobile, 2)
    order4_line2 = OrderLine(order4, car, 1)

    listofcustomer=[Suzuki,Puma,Classmate,Kinjal,Mital,Darshan,Sheetal,Dvijesh,Hardik]
    listoforder=[order1,order2,order3,order4]
    sorted_list = list(sorted(listoforder, key=lambda item: item.date))

    # displaying all customers
    print("------------------------------------------------------------------------------------------------------")
    print("Detail of valid customers")
    print("------------------------------------------------------------------------------------------------------")
    count = 1
    for i in listofcustomer:
        if i.name and i.email and i.phone and i.street and i.city and i.state and i.country and i.type:
            print()
            print("---------------")
            print(f"| Serial No. {count} |")
            print("---------------")
            count += 1
            i.display()
        else:
            i.delobj()


    #dispalying sorted orders
    print()
    print("------------------------------------------------------------------------------------------------------")
    print("Detail of orders sorted by date")
    print("------------------------------------------------------------------------------------------------------")


    count=1
    for i in sorted_list:
        print()
        print("----------------")
        print(f"|Order No. {count} |")
        print("-------------")
        count+=1
        i.display()
        print("\n\n")

    #display all orders of a product
    search_product=input("Enter product name:")
    flag=0
    print("--------------------------------------")
    print("| List of orders of specific product |")
    print("--------------------------------------")
    for i in listofproduct:
        if i.name==search_product:
            for j in listoforder:
                for k in j.order_lines:
                    if k.product==i:
                        print()
                        print("Order number:",j.number)
                        k.display()
                        flag=1
    if flag==0:
        print()
        print("No such product order!")

    #filter current month orders
    print("\n\n")
    user=input("Do you want current month orders? yes/no")
    if user=='yes':
        count=1
        for i in listoforder:
            if i.date.month==datetime.today().month:
                print("\n")
                print("--------------------")
                print(f"|Order No. {count} |")
                print("-------------------------")
                count+=1
                i.display()
    elif user=='no':
        pass
    else:
        print("Invalid input")

    '''#search order from order number
    print("\n\n")
    search_order = int(input("Enter Order Number: "))
    flag = 0
    for i in listoforder:
        if i.number == search_order:
            i.display()
            flag = 1
    if flag == 0:
        print("No such orders!")'''


    '''#search using binary search
    def search(lst, target):
        temp1 = 0
        min = 0
        max = len(lst) - 1
        avg = (min + max) // 2
        while (min <= max):
            if (str(lst[avg].number) == str(target)):
                lst[avg].display()
                temp1 = 1
                break
            elif (float(lst[avg].number) < float(target)):
                return search(lst[avg + 1], target)
            else:
                return search(lst[:avg], target)

        if temp1 == 0:
            print("not available order number ")

    sorted_list=list(sorted(listoforder,key=lambda i:i.number))
    order_number=int(input("Enter order number:"))
    search(sorted_list,order_number)'''

    #search oreder using binary search
    sorted_list2=list(sorted(listoforder,key=lambda item:item.number))
    search_order=input("Enter order number:")
    high=len(sorted_list2)-1
    low=0
    Order.binary_search(sorted_list2,low,high,search_order)


if __name__=='__main__':
    main()
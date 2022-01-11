import re
from datetime import datetime,date
from E001_V2 import Product,Category

#create customer class
class Customer:

    #define member of customer
    def __init__(self,name,email,phone,street,city,state,country,type=None,company=None):
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
            print(self.type)
        else:
            print("Enter valid type")

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
    def display_customer_detail(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Phone:",self.phone)
        print("Street:",self.street)
        print("City:",self.city)
        print("State:",self.state)
        print("Country:",self.country)
        print("Company",self.company)
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
        if billing.type=='billing' and shipping.type=='shipping':
            self.billing=billing
            self.shipping=shipping
        else:
            print("Please check type")

    #date validation
    def check(self,date1):
        try:
            date_obj=datetime.strptime(date1,'%Y-%m-%d')
            if date_obj.date()<date.today():
                print("Past date is not valid")
            else:
                return date_obj
        except Exception as e:
            print(e)

    #display order details
    def display_order(self):
        print("Number:",self.number)
        print("Date:",self.date)
        print("Company",self.comapny)
        print("Billing:",self.billing)
        print("Shipping",self.shipping)
        print("Order Lines:",self.order_lines)
        for i in self.order_lines:
            print(i.order.number)


#create orderline class
class OrderLine:

    #define member of orderline class
    def __init__(self,order,product,quantity):
        self.order=order
        self.product=product
        self.quantity=quantity
        self.price=product.price
        self.subtotal=self.price*quantity
        self.order.order_lines.append(self)


#main function
def main():
    Into = Customer("Into", '1into2@gmail.com', '919429118530', 'Ayodhyachock', 'Rajkot', 'Gujarat', 'India', "company")
    Dhara = Customer("Dhara", '.12@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India', "billing",Into)
    yudiz = Customer("yudiz", '.12@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India', "shipping",Into)
    Dharti = Customer("Dharti", '.12@gmail.com', '919426519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India', "contact")

    Vehical=Category('Vehical')
    Electronic=Category('Electronic')
    Stationary=Category('Stationary')

    mobile=Product("Mobile",Electronic,15000)
    car=Product("Car",Vehical,800000)
    book=Product("Book",Stationary,100)
    pen=Product("Pen",Stationary,20)

    order1 = Order('2022-02-25', Into, Dhara, yudiz)
    order2 = Order('2022-05-02', Into, Dhara, yudiz)
    order3 = Order('2025-09-09', Into, Dhara, yudiz)

    orderline1 = OrderLine(order1, mobile, 10)
    orderline2 = OrderLine(order2, book, 2)
    orderline3 = OrderLine(order3, car, 2)

    Into.display_customer_detail()
    order1.display_order()
    print()
    order2.display_order()


if __name__=='__main__':
    main()





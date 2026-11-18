# # 1. Student Management System
# class Student:
#     def __init__(self,name,roll_no,mark):
#         self.name=name
#         self.roll_no=roll_no
#         self.mark=mark
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Roll_no: {self.roll_no}")
#         print(f"Mark: {self.mark}")
#     def grade(self):
#         if self.mark>=90:
#             print("Grade: A")
#         elif self.mark>=75:
#             print("Grade: B")
#         elif self.mark>=50:
#             print("Grade: C")
#         else:
#             print("Fail")

# s1=Student("Abi",1,80)
# s2=Student("Anu",5,45)
# s3=Student("Sree",30,92)

# s1.display()
# s2.display()
# s3.display()


# # 2. Bank Account System
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid deposit amount")
#         else:
#             self.balance += amount
#             print("Amount deposited successfully")
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid withdrawal amount")
#         elif amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print("Amount withdrawn successfully")
#     def display_balance(self):
#         print("Account Holder:", self.account_holder)
#         print("Final Balance:", self.balance)

# account = BankAccount("Anu", 5000)

# account.deposit(2000)
# account.withdraw(1000)
# account.withdraw(8000)
# account.deposit(-500)
# account.withdraw(0)
# account.display_balance()


# # 3. Employee Salary Calculator
# class Employee:
#     def __init__(self, emp_id, name, basic_salary, department):
#         self.emp_id = emp_id
#         self.name = name
#         self.basic_salary = basic_salary
#         self.department = department
#     def calculate_hra(self):
#         return self.basic_salary * 0.20
#     def calculate_da(self):
#         return self.basic_salary * 0.10
#     def calculate_gross_salary(self):
#         hra = self.calculate_hra()
#         da = self.calculate_da()
#         return self.basic_salary + hra + da
#     def display_report(self):
#         print("Employee salary report")
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Department:", self.department)
#         print("Basic Salary:", self.basic_salary)
#         print("HRA:", self.calculate_hra())
#         print("DA:", self.calculate_da())
#         print("Gross Salary:", self.calculate_gross_salary())

# emp1 = Employee(101, "Anu", 30000, "IT")

# emp1.display_report()



# # 4.Product Inventory Management
# class Product:
#     def __init__(self, product_id, name, price, quantity):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def inventory_value(self):
#         return self.price * self.quantity
#     def sell(self, qu):
#         if qu <= 0:
#             print("Invalid quantity")
#         elif qu > self.quantity:
#             print("Not enough stock available")
#         else:
#             self.quantity -= qu
#             print(qu, "items sold successfully")
#     def restock(self, qu):
#         if qu <= 0:
#             print("Invalid restock quantity")
#         else:
#             self.quantity += qu
#             print(qu, "items added to stock")
#     def display(self):
#         print("Product Details")
#         print("Product ID:", self.product_id)
#         print("Name:", self.name)
#         print("Price:", self.price)
#         print("Available Quantity:", self.quantity)
#         print("Total Inventory Value:", self.inventory_value())

# p1 = Product(101, "Laptop", 50000, 10)

# p1.display()
# p1.sell(3)
# p1.sell(15)
# p1.restock(5)
# p1.display()



# # 5.Library Book Management System
# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.available = True
#     def borrow_book(self):
#         if self.available:
#             self.available = False
#             print(self.title, "has been borrowed successfully")
#         else:
#             print(self.title, "is currently not available")
#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print(self.title, "has been returned successfully")
#         else:
#             print(self.title, "was not borrowed")
#     def display(self):
#         print("\nTitle:", self.title)
#         print("Author:", self.author)
#         print("ISBN:", self.isbn)
#         if self.available:
#             print("Status: Available")
#         else:
#             print("Status: Borrowed")

# b1 = Book("aaa", "aaa", "ISBN101")
# b2 = Book("bbb", "bbb", "ISBN102")
# b3 = Book("ccc", "ccc", "ISBN103")
# b4 = Book("ddd", "ddd", "ISBN104")
# b5 = Book("eee", "eee", "ISBN105")

# books = [b1, b2, b3, b4, b5]
# print("Initial Book Availability")
# for book in books:
#     book.display()
# print("\nBorrowing Books")
# b1.borrow_book()
# b1.borrow_book() 
# print("\nReturning Books")
# b1.return_book()
# print("\nUpdated Book Availability")
# for book in books:
#     book.display()



# # 6.Vehicle Rental System
# class Vehicle:
#     def __init__(self, vehicle_id, brand, rent_per_day):
#         self.vehicle_id = vehicle_id
#         self.brand = brand
#         self.rent_per_day = rent_per_day
#     def calculate_rent(self, days):
#         return self.rent_per_day * days

# class Car(Vehicle):
#     def calculate_rent(self, days):
#         rent = self.rent_per_day * days
#         service_charge = rent * 0.10
#         total = rent + service_charge
#         return total

# class Bike(Vehicle):
#     def calculate_rent(self, days):
#         rent = self.rent_per_day * days
#         service_charge = rent * 0.05
#         total = rent + service_charge
#         return total

# class Truck(Vehicle):
#     def calculate_rent(self, days):
#         rent = self.rent_per_day * days
#         loading_charge = 500
#         total = rent + loading_charge
#         return total
    
# car1 = Car(101, "Toyota", 2000)
# bike1 = Bike(102, "Honda", 500)
# truck1 = Truck(103, "Tata", 5000)

# days = 3

# vehicles = [car1, bike1, truck1]
# for vehicle in vehicles:
#     print("\nVehicle ID:", vehicle.vehicle_id)
#     print("Brand:", vehicle.brand)
#     print("Rent per Day:", vehicle.rent_per_day)
#     total = vehicle.calculate_rent(days)
#     print("Rental Days:", days)
#     print("Total Rent:", total)



# # 7.Employee Hierarchy
# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary
#     def calculate_bonus(self):
#         return 0
#     def display_salary(self):
#         bonus = self.calculate_bonus()
#         total_salary = self.base_salary + bonus
#         print("\nEmployee Name:", self.name)
#         print("Base Salary:", self.base_salary)
#         print("Bonus:", bonus)
#         print("Total Salary:", total_salary)

# class Manager(Employee):
#     def __init__(self, name, base_salary):
#         super().__init__(name, base_salary)
#     def calculate_bonus(self):
#         return self.base_salary * 0.20

# class Developer(Employee):
#     def __init__(self, name, base_salary):
#         super().__init__(name, base_salary)
#     def calculate_bonus(self):
#         return self.base_salary * 0.15
    
# class Intern(Employee):
#     def __init__(self, name, base_salary):
#         super().__init__(name, base_salary)
#     def calculate_bonus(self):
#         return self.base_salary * 0.05

# m1 = Manager("Anu", 50000)
# d1 = Developer("Rahul", 40000)
# i1 = Intern("Arun", 15000)

# employees = [m1, d1, i1]
# for emp in employees:
#     emp.display_salary()


# # 8.Shape Area Calculator
# import math
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height

# c1 = Circle(5)
# r1 = Rectangle(10, 5)
# t1 = Triangle(8, 6)

# shapes = [c1, r1, t1]
# for shape in shapes:
#     print("Area:",shape.area())


# # 9.Online Shopping Cart
# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price

# class ShoppingCart:
#     def __init__(self):
#         self.cart_products = []
#     def add_product(self, product):
#         self.cart_products.append(product)
#         print(product.name, "added to cart")
#     def remove_product(self, product_id):
#         for product in self.cart_products:
#             if product.product_id == product_id:
#                 self.cart_products.remove(product)
#                 print(product.name, "removed from cart")
#                 return
#         print("Product not found")
#     def calculate_total(self):
#         total = 0
#         for product in self.cart_products:
#             total += product.price
#         return total
#     def generate_bill(self):
#         print("\nShopping Cart Bill")
#         if not self.cart_products:
#             print("Your cart is empty")
#             return
#         for product in self.cart_products:
#             print(product.name, "-", product.price)
#         total = self.calculate_total()
#         print("Subtotal: ", total)
#         if total > 5000:
#             discount = total * 0.10
#         else:
#             discount = 0
#         final_total = total - discount
#         print("Discount: ", discount)
#         print("Final Amount: ", final_total)

# p1 = Product(101, "Laptop", 40000)
# p2 = Product(102, "Mouse", 500)
# p3 = Product(103, "Keyboard", 1500)
# p4 = Product(104, "Headphones", 2000)

# cart = ShoppingCart()
# cart.add_product(p1)
# cart.add_product(p2)
# cart.add_product(p3)
# cart.add_product(p4)
# cart.remove_product(103)
# cart.generate_bill()


# 10.# Employee ID Generator

class Employee:
    employee_count = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Employee.employee_count += 1
        self.employee_id = f"EMP{Employee.employee_count:03d}"
    def display_details(self):
        print("\nEmployee ID:", self.employee_id)
        print("Name:", self.name)
        print("Email:", self.email)
    @classmethod
    def display_total_employees(cls):
        print("\nTotal Employees:", cls.employee_count)
    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False

e1 = Employee("Anu", "anu@gmail.com")
e2 = Employee("Rahul", "rahul@gmail.com")
e3 = Employee("Arun", "arun@gmail.com")
e1.display_details()
e2.display_details()
e3.display_details()

Employee.display_total_employees()

email = "test@gmail.com"
if Employee.validate_email(email):
    print("\nValid Email Address")
else:
    print("\nInvalid Email Address")
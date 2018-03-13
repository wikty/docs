from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Base, Person, Address, Department, Employee, Order, Item, OrderItem, User, ShoppingCart, Product, ShoppingCartProductLink
 
engine = create_engine('sqlite:///example.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Insert a Person
# Note: before session commit, the model object's primary key is None
new_person = Person(name='new person')
print(new_person.id) # None
session.add(new_person)
print(new_person.id) # None
session.commit()
print(new_person.id) # some id

# Insert a Address belongs to the person
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()

# Insert Department and Employee
IT = Department(name="IT")
Financial = Department(name="Financial")
john = Employee(name="John")
john.department = IT
marry = Employee(name="marry", department=Financial)
cathy = Employee(name="Cathy", department=Financial)
session.add(IT)
session.add(Financial)
session.add_all([john, marry, cathy])
# session.rollback()
session.commit()

# Insert Order and Item
item1 = Item(name='apple', price=23.5)
item2 = Item(name='pear', price=12.8)
order1 = Order(name='20180101')
order2 = Order(name='20180102')
order1.items.append(item1) # order1/item1
item2.orders.append(order1) # order1/item2
order2.items.append(item2) # order2/item2
session.add(item1)
session.add(item2)
session.add(order1)
session.add(order2)
session.commit()

order = Order(name='00000001')
item1 = Item(name='apple1', price=2.5)
item2 = Item(name='pear1', price=1.8)
oi = OrderItem(order=order, item=item1, item_count=2)
session.add(oi)
oi = OrderItem(order=order, item=item2, item_count=5)
session.add(oi)
session.commit()


# Insert User, Product, ShoppingCart
john = User(name='john')
cpu = Product(name='CPU', price=300.00)
motherboard = Product(name='Motherboard', price=150.00)
coffee_machine = Product(name='Coffee Machine', price=30.00)
john_shopping_cart_computer = ShoppingCart(owner=john)
john_shopping_cart_kitchen = ShoppingCart(owner=john)
john_shopping_cart_computer.products.append(cpu)
john_shopping_cart_computer.products.append(motherboard)
john_shopping_cart_kitchen.products.append(coffee_machine)
session.add(john)
session.add(cpu)
session.add(motherboard)
session.add(coffee_machine)
session.add(john_shopping_cart_computer)
session.add(john_shopping_cart_kitchen)
session.commit()
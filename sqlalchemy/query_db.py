from datetime import datetime

from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func, and_, not_, or_, text

from models import Base
from models import Address, Person
from models import Employee, Department
from models import Order, Item, OrderItem
from models import User, ShoppingCart, Product, ShoppingCartProductLink


# Engine
engine = create_engine('sqlite:///example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# Session
# A Session establishes and maintains all conversations between your program and the databases. It represents an intermediary zone for all the Python model objects you have loaded in it. It is one of the entry points to initiate a query against the database, whose results are populated and mapped into unique objects within the Session.
# Lifespan of a Session
# 1. A Session is constructed, at which point it is not associated with any model objects.
# 2. The Session receives query requests, whose results are persisted / associated with the Session.
# 3. Arbitrary number of model objects are constructed and then added to the Session, after which point the Session starts to maintain and manage those objects.
# 4. Once all the changes are made against the objects in the Session, we may decide to commit the changes from the Session to the database or rollback those changes in the Session. Session.commit() means that the changes made to the objects in the Session so far will be persisted into the database while Session.rollback() means those changes will be discarded.
# 5. Session.close() will close the Session and its corresponding connections, which means we are done with the Session and want to release the connection object associated with it
# States of model objects in a Session
# Transient: an instance that's not included in a session and has not been persisted to the database.
# Pending: an instance that has been added to a session but not persisted to a database yet. It will be persisted to the database in the next session.commit().
# Persistent: an instance that has been persisted to the database and also included in a session. You can make a model object persistent by committing it to the database or query it from the database.
# Detached: an instance that has been persisted to the database but not included in any sessions.

# Construct a sessionmaker object and bind the sessionmaker to engine
DBSession = sessionmaker(bind=engine)
# Make a new Session object
# A session establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
# If you call sessionmaker() a second time, you will get a new session object whose states are independent of the previous session.
# and you cannot add the same model object into different session objects
session = DBSession()

## CRUD
# # retrieve
# person = session.query(Person).filter(Person.name == 'new person').one()
# # update
# person.name = 'tom'
# session.commit()
# # delete
# print(inspect(person)) # inspect model object state
# session.delete(person)
# session.commit()
# print(inspect(person)) # inspect model object state

# one-to-many
print(session.query(Person).all())
person = session.query(Person).first()
print(person.name)

print(session.query(Person).count())

print(session.query(Address).filter(Address.person == person).all())
address = session.query(Address).filter(Address.person == person).one()
print(address.post_code)

department = session.query(Department).filter(Department.name == 'IT').all()[0]
print(department.employees[0].name)

print(session.query(Employee).filter(Employee.name.startswith('C')).first().name)

print(session.query(Employee).join(Employee.department).filter(Employee.name.startswith('C'), Department.name == 'Financial').all()[0].name)

print(session.query(Employee).filter(Employee.hired_on >= func.now()).count())
print(session.query(Employee).filter(Employee.hired_on < func.now()).count())

# many-to-many
order = session.query(Order).filter(Order.id == 1).one()
print(order.items)

item = session.query(Item).filter(Item.id == 1).one()
print(item.orders)

for name, price in session.query(Item.name, Item.price):
    print('Item: ', name, price)

for row in session.query(Item.name, Item.price):
    print('Item: ', row.name, row.price)

for row in session.query(Item).order_by(Item.price)[1:3]:
    print(row)

for row in session.query(Item).filter_by(name='dd'):
    print(row)

for row in session.query(Item).filter(Item.name.like('%dd%')):
    print(row)

for row in session.query(Item).filter(Item.name.ilike('%dd%')):
    print(row)

for row in session.query(Item).filter(Item.name.in_(['dd', 'hh', 'k'])):
    print(row)

for row in session.query(Item).filter(~Item.name.in_(['dd', 'hh', 'k'])):
    print(row)

for row in session.query(Item).filter(Item.name.is_(None)):
    print(row)

for row in session.query(Item).filter(Item.name.isnot(None)):
    print(row)

for row in session.query(Item).filter(text('id>3')).order_by(text('id')):
    print(row)

for row in session.query(Item).filter(text('id>:value and name=:name')).params(value=2, name='dd').order_by(text('id')):
    print(row)

for row in session.query(Item).filter(Item.name=='dd').filter(Item.price>1.2):
    print(row)

for row in session.query(Item).filter(and_(Item.name=='dd', Item.price>1.2)):
    print(row)

for row in session.query(Item).filter(or_(Item.name=='dd', Item.price>1.2)):
    print(row)


query = session.query(User).filter(User.name.like('%xx%')).order_by(User.id)
print(query.all())
print(query.first())
# print(query.one()) # not found, raise exception
print(query.one_or_none())
print(query.scalar())

print(session.query(User).filter(User.name.like('%xx%')).count())


# which order has item1
orders = session.query(Order).filter(Order.items.any(Item.id == 1)).all()
print(orders)

# order1 has which items
items = session.query(Item).filter(Item.orders.any(Order.id == 1)).all()
print(items)

oi = session.query(OrderItem).join(Item).filter(Item.name == 'apple1').first()
print(oi.order.name, oi.item.name, oi.item.price, oi.item_count)

# sqlalchemy expression language provides lower-level Python structures that mimic a backend-neutral SQL, it feels almost identical to writing actual SQL but in a Pythonic way.
find_it = select([Department.id, Department.name]).where(Department.name == 'IT')
rs = session.execute(find_it)
print(rs.fetchone())
find_tom = select([Employee.id, Employee.name]).where(Employee.department_id == 1)
rs = session.execute(find_tom)
print(rs.fetchone())

# which products' prices are higher than $100.00?
el1 = select([Product.id]).where(Product.price > 100)
rs = session.execute(el1)
print(rs.fetchone())
# which shopping carts contain at least one product whose price is higher than $100.00?
el2 = select([ShoppingCart.id]).where(
    ShoppingCart.products.any(Product.price > 100)
)
print(session.query(ShoppingCart).filter(ShoppingCart.id.in_(el2)).first())
# which shopping carts contain no product whose price is lower than $100.00?
el3 = select([ShoppingCart.id]).where(
    not_(ShoppingCart.products.any(Product.price > 100))
)
print(session.query(ShoppingCart).filter(ShoppingCart.id.in_(el3)).first())
# how can we find the shopping carts all of whose products have a price higher than $100.00?
el4 = select([ShoppingCart.id]).where(
    and_(
        ShoppingCartProductLink.product_id.in_(el1),
        ShoppingCartProductLink.shopping_cart_id == ShoppingCart.id
    )
)
print(session.query(ShoppingCart).filter(ShoppingCart.id.in_(el4)).first())
# which shopping carts' total price of the products is higher than $200.00?
el5 = select([
    ShoppingCart.id.label('shopping_cart_id'),
    func.sum(Product.price).label('product_price_sum')
]).where(
    and_(
        ShoppingCartProductLink.product_id == Product.id,
        ShoppingCartProductLink.shopping_cart_id == ShoppingCart.id
    )
).group_by(ShoppingCart.id)
print(session.query(el5).all()) # total
print(session.query(ShoppingCart).filter(
    el5.c.shopping_cart_id == ShoppingCart.id,
    el5.c.product_price_sum > 200
).all())

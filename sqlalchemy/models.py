from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

# One-to-One Model: Person >---< Address

class Person(Base):
    '''
    each person has only one address
    '''
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Address(Base):
    '''
    each address belongs to one person
    '''
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    # set uselist to False, so that the models' relationship is one-to-one
    person = relationship(
        Person, backref=backref('address', uselist=False)
    )

# One-to-Many Model: Department ---<< Employee

class Department(Base):
    '''
    one department has many employees
    '''
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Employee(Base):
    '''
    each employee belongs to one department
    '''
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # set the default hiring time as current time
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # the cascade allows SQLAlchemy to automatically delete a department's employees when the department itself is deleted.
    # the userlist is True, so that the models' relationship is one-to-many
    department = relationship(
        Department, 
        backref=backref('employees', uselist=True, cascade='delete,all')
    )

# One-to-Many Model: Blogger ---<< Post

class Blogger(Base):
    '''
    using two relationships to specify the one-to-many mapping
    '''
    __tablename__ = 'blogger'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content = Column(String(256))
    owner_id = Column(Integer, ForeignKey('blogger.id'))
    owner = relationship("Blogger", back_populates="posts")


# Many-to-Many Model: Order >>---<< Item

class Order(Base):
    '''
    each order has many items
    '''
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # 'Item' not Item, because Item define in the following
    items = relationship('Item', secondary='order_item')

class Item(Base):
    '''
    every item belongs to more than one order
    '''
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    orders = relationship('Order', secondary='order_item')

class OrderItem(Base):
    '''
    the Association Table for order&item
    '''
    __tablename__ = 'order_item'
    # foreign keys of association table, for relationship many-to-many
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)
    # extra keys of association table, for other storage data
    item_count = Column(Integer)
    order = relationship(Order, backref=backref('order_associated'))
    item = relationship(Item, backref=backref('item_associated'))

# Shopping Example
# One-to-Many Model: User ---<< ShoppingCart
# Many-to-Many Model: ShoppingCart >>---<< Product

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
  
class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey(User.id))
    owner = relationship(
        User, backref=backref('shopping_carts', uselist=True)
    )
    products = relationship(
        'Product',
        secondary='shopping_cart_product_link'
    )

    def __repr__(self):
        return '( {0}:{1.owner.name}:{1.products!r} )'.format(ShoppingCart, self)
  
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    shopping_carts = relationship(
        'ShoppingCart',
        secondary='shopping_cart_product_link'
    )

    def __repr__(self):
        return '( {0}:{1.name!r}:{1.price!r} )'.format(Product, self)  

class ShoppingCartProductLink(Base):
    __tablename__ = 'shopping_cart_product_link'
    shopping_cart_id = Column(Integer, ForeignKey('shopping_cart.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)


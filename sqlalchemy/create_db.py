from sqlalchemy import create_engine

from models import Base

# Create an engine that stores data in the local directory's example.db
engine = create_engine('sqlite:///example.db')
 
# Create all tables in the database which are defined by Base's subclass. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
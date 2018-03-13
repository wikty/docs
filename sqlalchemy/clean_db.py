from sqlalchemy import create_engine, MetaData

from models import Base

 
engine = create_engine('sqlite:///example.db')
meta = MetaData()
meta.reflect(bind=engine)

for tbl in reversed(meta.sorted_tables):
    engine.execute(tbl.delete())

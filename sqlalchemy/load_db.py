from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///example.db')

# load a table from database
meta = MetaData(bind=engine)
person = Table("person", meta, autoload=True, autoload_with=engine)
print([c.name for c in person.columns])

# load all of tables from database
meta = MetaData()
meta.reflect(bind=engine)
for tblname in meta.tables:
    print(tblname, [c.name for c in meta.tables[tblname].columns])
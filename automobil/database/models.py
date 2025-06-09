from sqlalchemy import inspect, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from automobil.settings import Settings

engine = create_engine(Settings().DATABASE_URL)
Base = declarative_base()

class Automobile(Base):
    __tablename__ = "automobiles"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(String(4))
    model = Column(String, index=True)
    color = Column(String)
    manufacturer = Column(String)
    motor = Column(String)
    fuel = Column(String)
    price = Column(String)
    kilometers = Column(Integer)
    transmission = Column(String)
    number_of_wheels = Column(Integer)

def create_db_and_tables():
    inspector = inspect(engine)
    defined_table_names = list(Base.metadata.tables.keys())

    if not defined_table_names:
        Base.metadata.create_all(engine)
        return False

    all_tables_existed_before = True
    for table_name in defined_table_names:
        if not inspector.has_table(table_name):
            all_tables_existed_before = False
            break
    
    Base.metadata.create_all(engine)

    return not all_tables_existed_before
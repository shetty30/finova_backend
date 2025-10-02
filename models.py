from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///database.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()

class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    category = Column(String)
    amount = Column(Float)

class Savings(Base):
    __tablename__ = "savings"
    id = Column(Integer, primary_key=True)
    goal = Column(Float)

Base.metadata.create_all(engine)

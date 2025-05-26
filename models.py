from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

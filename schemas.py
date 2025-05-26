from pydantic import BaseModel

class SupplierBase(BaseModel):
    name: str
    contact: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    quantity: int
    supplier_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

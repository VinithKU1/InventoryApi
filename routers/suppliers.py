from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Supplier])
def read_suppliers(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)

@router.post("/", response_model=schemas.Supplier)
def add_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db, supplier)

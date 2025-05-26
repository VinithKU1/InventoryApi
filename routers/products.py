from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.post("/", response_model=schemas.Product)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

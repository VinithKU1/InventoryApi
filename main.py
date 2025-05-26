from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from routers import products, suppliers

# Create all tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Inventory Management API")

# CORS setup: allow all devices on your LAN (including mobile) to access and modify the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later for security
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

# Include your API routers
app.include_router(suppliers.router)
app.include_router(products.router)

# Serve frontend (e.g., index.html) from 'frontend' folder at root URL
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

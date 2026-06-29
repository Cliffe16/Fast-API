from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Locate Database
DATABASE_URL = "sqlite:///./appointments.db"

# Create database connection engine with concurrent connection
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session bound to our db connection
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    """This function initializes a db session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

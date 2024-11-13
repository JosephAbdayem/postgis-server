from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for ORM models
Base = declarative_base()

# Database connection URL
DATABASE_URL = "postgresql+psycopg2://geoserver:geoserver_password@localhost:5432/geodata"

# Create the SQLAlchemy engine connected to the database
engine = create_engine(DATABASE_URL)

# Session factory for creating new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

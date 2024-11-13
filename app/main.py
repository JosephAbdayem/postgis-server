from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db.database import engine, Base, SessionLocal
from app.models.point import Point
from app.models.polygon import Polygon
from app.schemas.point import PointCreate
from app.schemas.polygon import PolygonCreate
from geoalchemy2.elements import WKTElement

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()


def get_db():
    """Provide a database session to route handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    """
    Root endpoint to confirm the service is running.

    Returns:
        dict: A simple JSON message.
    """
    return {"Hello": "World"}


@app.post("/points/", response_model=dict)
def create_point(point: PointCreate, db: Session = Depends(get_db)):
    """
    Create a new Point in the database.

    Args:
        point (PointCreate): The point data including name and geometry in WKT format.
        db (Session): Database session dependency.

    Returns:
        dict: Confirmation message with the created Point ID.
    """
    db_point = Point(name=point.name, geom=WKTElement(point.geom, srid=4326))
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return {"message": "Point created successfully", "point": db_point.id}


@app.post("/polygons/", response_model=dict)
def create_polygon(polygon: PolygonCreate, db: Session = Depends(get_db)):
    """
    Create a new Polygon in the database.

    Args:
        polygon (PolygonCreate): The polygon data including name and geometry in WKT format.
        db (Session): Database session dependency.

    Returns:
        dict: Confirmation message with the created Polygon ID.
    """
    db_polygon = Polygon(
        name=polygon.name, geom=WKTElement(polygon.geom, srid=4326))
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return {"message": "Polygon created successfully", "polygon": db_polygon.id}

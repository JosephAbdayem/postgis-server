from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from app.db.database import Base


class Polygon(Base):
    """
    Represents a polygon entity in the spatial database.

    Attributes:
        id (int): The unique identifier of the polygon.
        name (str): The name of the polygon, cannot be null.
        geom (Geometry): The geometry column storing the polygon shape, using SRID 4326.
    """
    __tablename__ = 'polygon'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # Spatial data for polygon
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326))

from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from app.db.database import Base


class Point(Base):
    """
    Represents a point entity in the spatial database.

    Attributes:
        id (int): The unique identifier of the point.
        name (str): The name of the point, cannot be null.
        geom (Geometry): The geometry column storing the point location, using SRID 4326.
    """
    __tablename__ = 'point'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # Spatial data for point
    geom = Column(Geometry(geometry_type='POINT', srid=4326))

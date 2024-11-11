from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from app.db.database import Base


class Point(Base):
    __tablename__ = 'point'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))

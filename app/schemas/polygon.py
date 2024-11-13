from pydantic import BaseModel


class PolygonCreate(BaseModel):
    """
    Schema for creating a new Polygon entry.

    Attributes:
        name (str): The name of the polygon.
        geom (str): The geometry of the polygon in WKT format, e.g., 'POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))'.
    """
    name: str
    geom: str

    class Config:
        """Configuration to allow Pydantic model compatibility with SQLAlchemy ORM."""
        orm_mode = True

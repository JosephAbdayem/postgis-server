from pydantic import BaseModel


class PointCreate(BaseModel):
    """
    Schema for creating a new Point entry.

    Attributes:
        name (str): The name of the point.
        geom (str): The geometry of the point in WKT format, e.g., 'POINT(30 10)'.
    """
    name: str
    geom: str

    class Config:
        """Configuration to allow Pydantic model compatibility with SQLAlchemy ORM."""
        orm_mode = True

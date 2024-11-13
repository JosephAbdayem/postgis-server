"""create points and polygons tables

Revision ID: 98c010dc225e
Revises: 
Create Date: 2024-11-12 21:42:43.449976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = '98c010dc225e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the 'point' table
    op.create_table(
        'point',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT',
                  srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    )

    # Conditionally create the GIST index on 'geom' column for 'point' table
    if not op.get_bind().dialect.has_index(op.get_bind(), 'point', 'idx_point_geom'):
        op.create_index('idx_point_geom', 'point', [
                        'geom'], unique=False, postgresql_using='gist')

    # Create the 'polygon' table
    op.create_table(
        'polygon',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POLYGON',
                  srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    )

    # Conditionally create the GIST index on 'geom' column for 'polygon' table
    if not op.get_bind().dialect.has_index(op.get_bind(), 'polygon', 'idx_polygon_geom'):
        op.create_index('idx_polygon_geom', 'polygon', [
                        'geom'], unique=False, postgresql_using='gist')


def downgrade() -> None:
    # Drop the GIST index on 'geom' column for 'point' table if it exists
    if op.get_bind().dialect.has_index(op.get_bind(), 'point', 'idx_point_geom'):
        op.drop_index('idx_point_geom', table_name='point')

    # Drop the 'point' table
    op.drop_table('point')

    # Drop the GIST index on 'geom' column for 'polygon' table if it exists
    if op.get_bind().dialect.has_index(op.get_bind(), 'polygon', 'idx_polygon_geom'):
        op.drop_index('idx_polygon_geom', table_name='polygon')

    # Drop the 'polygon' table
    op.drop_table('polygon')

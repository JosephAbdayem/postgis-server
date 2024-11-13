import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# Importing models to ensure they are included in Alembic's migration tracking
from app.models import point, polygon  # Keep
from app.db.database import Base

# Add the app directory to the system path to allow model imports
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../app')))

# Load configuration from the Alembic configuration file
config = context.config

# Set up logging configuration from the config file
fileConfig(config.config_file_name)

# Set the target metadata to reflect models within the Alembic context
target_metadata = Base.metadata


def run_migrations_online():
    """
    Runs migrations in 'online' mode.

    In online mode, Alembic connects directly to the database to apply migrations.
    The database connection settings are retrieved from the Alembic configuration.
    """
    # Create a database engine from Alembic configuration settings
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Establish a connection to the database and configure migration context
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # Ensures Alembic detects type changes in columns
        )

        # Begin a migration transaction
        with context.begin_transaction():
            context.run_migrations()


# Execute the migration function to apply migrations
run_migrations_online()

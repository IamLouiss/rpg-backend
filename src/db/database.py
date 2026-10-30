import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# Load environment variables (FastAPI loads .env automatically in dev mode)
# We use the port 5432
DB_USER = os.getenv("POSTGRES_USER", "rpg_admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Tobias2706*.")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "rpg_db")

# Construct the async connection URL for PostgreSQL
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@127.0.0.1:{DB_PORT}/{DB_NAME}"

# The Engine: Manages the connection pool to the database
# echo=true prints the generated SQL in the terminal which is useful for debugging
engine = create_async_engine(DATABASE_URL, echo=True)

# The Session: Represents a single short-lived database transaction
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# The base: The parent class for all our future database models
Base = declarative_base()

async def get_db():
    """
    Creates a new database session for a single request and closes it when done. 
    """
    async with AsyncSessionLocal() as session:
        yield session
"""
This module sets up the asynchronous database engine and session factory using SQLAlchemy.
It also provides a dependency for FastAPI routes to manage database sessions.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Ensure the DATABASE_URL uses asyncpg
engine = create_async_engine(settings.db_url, echo=True)

# Create the session factory for async sessions
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# Dependency for FastAPI routes
async def get_db():
    """
    Provides a database session for FastAPI routes.
    Ensures that the session is properly closed after use.
    Yields:
        AsyncSession: An asynchronous SQLAlchemy session.
    """
    async with AsyncSessionLocal() as session:
        yield session

# ==================== DATABASE SESSION SETUP ====================
# This file sets up the database connection engine and session factory
# It enables async database operations for better performance in FastAPI

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from app.core.config import settings

# ==================== DATABASE ENGINE ====================
# The engine is the central "hub" for database connectivity
# What it does:
#   - Manages connections to the database
#   - Provides connection pooling (reuses connections for efficiency)
#   - Executes SQL queries
#
# Why create_async_engine?
#   - Allows non-blocking database operations (async/await)
#   - Perfect for FastAPI which is built on async/await
#   - Multiple requests can query the database without blocking each other
#
# Parameters:
#   - settings.DATABASE_URL: Connection string (host, port, database name)
#   - echo=True: Logs all SQL queries to console (useful for debugging, turn off in production)
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# ==================== SESSION FACTORY ====================
# AsyncSessionLocal is a factory that creates new database sessions
# Think of it as a "session template" - not an actual session yet
#
# What it configures:
#   - engine: Which database to connect to
#   - class_=AsyncSession: Use async sessions (non-blocking operations)
#   - expire_on_commit=False: Keep loaded objects accessible after commit
#     (By default, SQLAlchemy refreshes data from DB after commit)
#
# How to use:
#   async with AsyncSessionLocal() as session:
#       # Now you have a database session ready to use
#       result = await session.execute(...)
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
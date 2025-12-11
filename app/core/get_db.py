# ==================== DATABASE DEPENDENCY INJECTION ====================
# This file provides a function that FastAPI uses to inject database sessions
# into route handlers automatically (dependency injection pattern)

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from app.core.session import AsyncSessionLocal

# ==================== GET_DB DEPENDENCY FUNCTION ====================
# This function is used by FastAPI to provide a database session to each request
#
# What it does:
#   1. Creates a new database session
#   2. Yields it to the route handler (endpoint function)
#   3. Automatically closes the session when the request is done
#
# Return type explanation:
#   - AsyncGenerator[AsyncSession, None]:
#     * AsyncGenerator: A generator that works with async/await
#     * AsyncSession: The type of object being yielded
#     * None: The second type parameter (not used here)
#
# How FastAPI uses it:
#   @app.get("/users")
#   async def get_users(db: AsyncSession = Depends(get_db)):
#       # FastAPI automatically calls get_db() and injects the session
#       result = await db.execute(...)
#       return result
#
# Why use yield instead of return:
#   - yield pauses execution and returns the session
#   - Code after yield runs AFTER the request completes
#   - This allows automatic cleanup (closing session)
#   - Equivalent to a try/finally block
#
# Why async/await:
#   - Allows non-blocking database operations
#   - Multiple requests can share the async event loop
#   - Better performance and resource usage
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    # Create a new database session using AsyncSessionLocal factory
    async with AsyncSessionLocal() as session:
        # Yield the session to the route handler
        # Execution pauses here until the endpoint finishes
        yield session
        # After the endpoint finishes, session automatically closes
        # (thanks to the async context manager 'async with')
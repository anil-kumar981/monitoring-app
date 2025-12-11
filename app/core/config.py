# ==================== CONFIGURATION MANAGEMENT ====================
# This file handles all application settings and configuration management
# using Pydantic BaseSettings for type-safe environment variable handling

import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# ==================== ENVIRONMENT DETECTION ====================
# Determine the current environment (development, staging, production)
# This helps load the appropriate .env file (e.g., .env.development)
ENV = os.getenv("ENV", "development")

# ==================== SETTINGS CLASS ====================
# This class defines all configuration variables needed for the application
# It automatically loads these values from environment variables or .env files
class Settings(BaseSettings):
    
    # DATABASE_URL: Connection string for the database
    # Format: postgresql+asyncpg://user:password@host:port/database
    # asyncpg driver allows async database operations with SQLAlchemy
    DATABASE_URL: str

    # ==================== MODEL CONFIGURATION ====================
    # Configuration dictionary that tells Pydantic how to load settings
    model_config = SettingsConfigDict(
        # env_file: Path to the environment file to load
        # .env.development, .env.staging, .env.production etc.
        env_file=f".env.{ENV}",
        # env_file_encoding: Use UTF-8 encoding to read the .env file
        env_file_encoding="utf-8",
        # extra="ignore": Ignore any extra environment variables not defined in this class
        extra="ignore"
    )

# ==================== SETTINGS INSTANCE ====================
# Create a single instance of Settings that will be imported throughout the app
# This is a singleton pattern - one settings object used everywhere
settings = Settings()

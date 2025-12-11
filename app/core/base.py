# ==================== DATABASE BASE CONFIGURATION ====================
# This file sets up the base class for all SQLAlchemy ORM models

from sqlalchemy.orm import declarative_base

# ==================== DECLARATIVE BASE ====================
# Base is a special class that all database models will inherit from
# Why declarative_base?
#   - It tracks all model classes that inherit from it
#   - Allows SQLAlchemy to automatically map Python classes to database tables
#   - Enables automatic table creation using Base.metadata.create_all()
# 
# How it works:
#   1. Define a model class that inherits from Base (e.g., class User(Base))
#   2. SQLAlchemy automatically tracks table structure and column definitions
#   3. When creating tables, it uses metadata collected from all model classes
#
# Example usage:
#   class User(Base):
#       __tablename__ = "users"
#       id = Column(Integer, primary_key=True)
#       name = Column(String)
Base = declarative_base()
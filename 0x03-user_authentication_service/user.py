#!/usr/bin/env python3
"""
User model for SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for a user.

    Attributes:
        id (int): The primary key.
        email (str): The user's email address, non-nullable.
        hashed_password (str): The hashed password, non-nullable.
        session_id (str): The session ID, nullable.
        reset_token (str): The reset token, nullable.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

# Uncomment the following lines to create the table in the database.
# engine = create_engine('sqlite:///your_database.db')
# Base.metadata.create_all(engine)

#!/usr/bin/python3
"""
Defines a State class and creates an instance Base using SQLAlchemy.
The State class links to the MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table 'states'"""
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)


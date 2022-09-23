import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    favorites = relationship('Favorites')

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False) 
      
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    hair_color = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    children = relationship("Favorites")
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    hair_color = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    children= relationship("Favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
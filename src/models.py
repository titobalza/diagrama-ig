import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy.sql import func

time_created = Column(DateTime(timezone=True), server_default=func.now())
time_updated = Column(DateTime(timezone=True), onupdate=func.now())

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(250))
    post = relationship("Post")
    favorites = relationship("Favorites")
    comments = relationship("Comments") 
    followers = relationship("Followers")

    def update(self):
        return {}

class Likes(Base):
    __tablename__ = 'Likes'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    post_id = Column(Integer, ForeignKey('post.id'))
    

    def update(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    favorites = relationship("Favorites")

    def update(self):
        return {}

class Comments(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    favorites = relationship("Favorites")

    def serializer(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    from_user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    to_user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def serializer(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    def serializer(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
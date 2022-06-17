import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False)
    favorites = relationship('Favorite', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    climate = Column(String(32), nullable=True)
    population = Column(Integer, nullable=True)
    favorite_user = relationship('Favorite', backref='planets', lazy=True)
    favorite_character = relationship('Character', backref='planets', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    manufacturer = Column(String(64), nullable=True)
    max_speed = Column(Integer, nullable=True)
    favorite_user = relationship('Favorite', backref='vehicles', lazy=True)
    favorite_character = relationship('Character', backref='vehicles', lazy=True)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    eyes = Column(String(32), nullable=True)
    hair = Column(String(32), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    favorite_user = relationship('Favorite', backref='characters', lazy=True)


class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
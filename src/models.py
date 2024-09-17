import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(Date, index = True)

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planet_origin = Column(Integer, ForeignKey('planet.id'), nullable= False)
    height = Column(Float, nullable = False)
    weight = Column(Float, nullable = False)
    vehicle = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

    def to_dict(self):
        return {}
    

    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    density = Column(Float, nullable = False)
    weater = Column(String(250), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Float, nullable=False)

    def to_dict(self):
        return {}
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    model = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)
    crew = Column(Integer, nullable= False)

    def to_dict(self):
        return {}



class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    character = Column(Integer, ForeignKey('character.id'))
    director = Column(Integer, ForeignKey('director.id'))
    created = Column(Date, index=True)
    running_time= Column(Float, nullable=False)

    def to_dict(self):
        return {}


    
class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)

    def to_dict(self):
        return {}




class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"))
    planet = Column(Integer, ForeignKey("planet.id"),nullable = True)
    character = Column(Integer, ForeignKey("character.id"),nullable = True)
    vehicle = Column(Integer, ForeignKey("vehicle.id"),nullable = True)
    movie = Column(Integer, ForeignKey("movies.id"),nullable = True)
    
    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

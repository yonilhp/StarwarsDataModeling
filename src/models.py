from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er  # Importar render_er

Base = declarative_base()

# Modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    fecha_subscripcion = Column(DateTime, default=datetime.utcnow)

    # Relación Uno-a-Muchos con Favorito
    favoritos = relationship('Favorito', back_populates='usuario')

# Modelo Personaje
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))
    origen = Column(String(250))

    # Relación Uno-a-Muchos con Favorito
    favoritos = relationship('Favorito', back_populates='personaje')

# Modelo Planeta
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))
    clima = Column(String(250))

    # Relación Uno-a-Muchos con Favorito
    favoritos = relationship('Favorito', back_populates='planeta')

# Modelo Favorito
class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)

    # Relaciones con Usuario, Personaje y Planeta
    usuario = relationship('Usuario', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')

## Dibujar el diagrama ER
render_er(Base, 'diagram.png')

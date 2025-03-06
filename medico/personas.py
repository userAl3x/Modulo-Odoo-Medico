from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'PERSONAS'

    PK = Column(Integer, primary_key=True, autoincrement=True)
    MOM = Column(String(50), nullable=False)
    nombre = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    telefono = Column(String(15))
    seguencia = Column(Boolean, default=False)
    equipofrango = Column(Boolean, default=False)

    # Relación con EVENTOS (una persona pertenece a un evento)
    evento_id = Column(Integer, ForeignKey('EVENTOS.PK'))
    evento = relationship('Evento', back_populates='personas')

    def __repr__(self):
        return f"<Persona(PK={self.PK}, nombre={self.nombre}, apellidos={self.apellidos})>"
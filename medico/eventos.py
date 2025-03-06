from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Evento(Base):
    __tablename__ = 'EVENTOS'

    PK = Column(Integer, primary_key=True, autoincrement=True)
    MENewin = Column(String(255), nullable=False)
    Nerva = Column(Date, nullable=False)
    establecimiento = Column(String(255))
    direccion = Column(String(255))
    poblacion = Column(String(255))
    cadre = Column(String(255))
    notas = Column(Text)

    # Relación con PERSONAS (un evento puede tener varias personas asociadas)
    personas = relationship('Persona', back_populates='evento')

    def __repr__(self):
        return f"<Evento(PK={self.PK}, MENewin={self.MENewin}, Nerva={self.Nerva})>"
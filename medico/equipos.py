from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Equipo(Base):
    __tablename__ = 'EQUIPOS'

    PK = Column(Integer, primary_key=True, autoincrement=True)
    MÉRGIAICA = Column(String(255), nullable=False)
    regulatori = Column(Boolean, default=False)
    traje = Column(Boolean, default=False)
    challico = Column(Boolean, default=False)
    guerrilla = Column(Boolean, default=False)
    capotilla = Column(Boolean, default=False)
    caramarca = Column(Boolean, default=False)
    alerta = Column(Boolean, default=False)
    gafas = Column(Boolean, default=False)
    latero = Column(Boolean, default=False)

    # Relación con PERSONAS (un equipo puede tener varias personas asociadas)
    personas = relationship('Persona', back_populates='equipo')

    def __repr__(self):
        return f"<Equipo(PK={self.PK}, MÉRGIAICA={self.MÉRGIAICA})>"
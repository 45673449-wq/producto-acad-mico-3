# src/models.py
"""
Modelo simple para la tabla 'items' usando SQLAlchemy.
Diseñado para permitir usar diferentes engines (ej: sqlite:///:memory:)
en tests (para aislar la BD).
"""
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

# URL por defecto (usa archivo app.db si NO hay env var)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

def get_engine(url: str | None = None):
    """Devuelve un engine; si no se pasa url, usa DATABASE_URL."""
    return create_engine(url or DATABASE_URL, echo=False, future=True)

def init_db(engine=None):
    """Crear tablas (idempotente)."""
    engine = engine or get_engine()
    Base.metadata.create_all(engine)
    return engine

def get_session(engine=None):
    """Crear y devolver una sesión ligada al engine pasado (o al default)."""
    engine = engine or get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

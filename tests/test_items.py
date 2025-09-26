# tests/test_items.py
from src.models import get_engine, init_db, get_session, Item

def test_insert_and_query_item():
    # Usamos una BD en memoria para no tocar archivos en disco
    engine = get_engine("sqlite:///:memory:")
    init_db(engine)                 # crea las tablas en la BD en memoria
    session = get_session(engine)   # sesión ligada a ese engine

    # insertar
    new_item = Item(name="Borrador", description="Blanco")
    session.add(new_item)
    session.commit()

    # consultar
    saved = session.query(Item).filter_by(name="Borrador").first()
    assert saved is not None
    assert saved.description == "Blanco"

from src.models import Session, Item

def test_insert_and_query_item():
    session = Session()
    new_item = Item(name="Cuaderno", description="Cuadriculado")
    session.add(new_item)
    session.commit()

    saved = session.query(Item).filter_by(name="Cuaderno").first()
    assert saved is not None
    assert saved.description == "Cuadriculado"

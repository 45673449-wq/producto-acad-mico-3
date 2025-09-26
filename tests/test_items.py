from src.models import Session, Item

def test_insert_and_query_item():
    session = Session()

    # Insertar un item
    new_item = Item(name="Borrador", description="Blanco")
    session.add(new_item)
    session.commit()

    # Consultar el item
    saved = session.query(Item).filter_by(name="Borrador").first()
    assert saved is not None
    assert saved.description == "Blanco"

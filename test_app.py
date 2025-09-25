import pytest
import json
from sqlalchemy import create_engine
from app import create_app, Base

@pytest.fixture
def app():
    """Create a test app with in-memory SQLite database."""
    engine = create_engine('sqlite:///:memory:', connect_args={"check_same_thread": False})
    app = create_app(engine=engine)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test runner."""
    return app.test_cli_runner()

class TestItemAPI:
    """Test cases for the Item API endpoints."""
    
    def test_create_item_success(self, client):
        """Test creating an item successfully."""
        data = {"name": "Test Item", "description": "A test item"}
        response = client.post('/items', 
                             data=json.dumps(data),
                             content_type='application/json')
        assert response.status_code == 201
        json_data = json.loads(response.data)
        assert json_data['name'] == "Test Item"
        assert json_data['description'] == "A test item"
        assert 'id' in json_data
    
    def test_create_item_missing_name(self, client):
        """Test creating an item without required name field."""
        data = {"description": "A test item"}
        response = client.post('/items', 
                             data=json.dumps(data),
                             content_type='application/json')
        assert response.status_code == 400
        json_data = json.loads(response.data)
        assert json_data['error'] == 'name is required'
    
    def test_create_item_no_description(self, client):
        """Test creating an item without description."""
        data = {"name": "Test Item"}
        response = client.post('/items', 
                             data=json.dumps(data),
                             content_type='application/json')
        assert response.status_code == 201
        json_data = json.loads(response.data)
        assert json_data['name'] == "Test Item"
        assert json_data['description'] is None
    
    def test_get_item_success(self, client):
        """Test getting an item that exists."""
        # Create an item first
        data = {"name": "Test Item", "description": "A test item"}
        create_response = client.post('/items', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        item_id = json.loads(create_response.data)['id']
        
        # Get the item
        response = client.get(f'/items/{item_id}')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data['name'] == "Test Item"
        assert json_data['description'] == "A test item"
        assert json_data['id'] == item_id
    
    def test_get_item_not_found(self, client):
        """Test getting an item that doesn't exist."""
        response = client.get('/items/999')
        assert response.status_code == 404
        json_data = json.loads(response.data)
        assert json_data['error'] == 'not found'
    
    def test_list_items_empty(self, client):
        """Test listing items when none exist."""
        response = client.get('/items')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data == []
    
    def test_list_items_with_data(self, client):
        """Test listing items when some exist."""
        # Create two items
        data1 = {"name": "Item 1", "description": "First item"}
        data2 = {"name": "Item 2", "description": "Second item"}
        
        client.post('/items', data=json.dumps(data1), content_type='application/json')
        client.post('/items', data=json.dumps(data2), content_type='application/json')
        
        # List items
        response = client.get('/items')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert len(json_data) == 2
        assert json_data[0]['name'] == "Item 1"
        assert json_data[1]['name'] == "Item 2"
    
    def test_update_item_success(self, client):
        """Test updating an item successfully."""
        # Create an item first
        data = {"name": "Original Item", "description": "Original description"}
        create_response = client.post('/items', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        item_id = json.loads(create_response.data)['id']
        
        # Update the item
        update_data = {"name": "Updated Item", "description": "Updated description"}
        response = client.put(f'/items/{item_id}', 
                            data=json.dumps(update_data),
                            content_type='application/json')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data['name'] == "Updated Item"
        assert json_data['description'] == "Updated description"
        assert json_data['id'] == item_id
    
    def test_update_item_partial(self, client):
        """Test updating an item with partial data."""
        # Create an item first
        data = {"name": "Original Item", "description": "Original description"}
        create_response = client.post('/items', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        item_id = json.loads(create_response.data)['id']
        
        # Update only the name
        update_data = {"name": "Updated Item"}
        response = client.put(f'/items/{item_id}', 
                            data=json.dumps(update_data),
                            content_type='application/json')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data['name'] == "Updated Item"
        assert json_data['description'] == "Original description"  # Unchanged
    
    def test_update_item_not_found(self, client):
        """Test updating an item that doesn't exist."""
        update_data = {"name": "Updated Item"}
        response = client.put('/items/999', 
                            data=json.dumps(update_data),
                            content_type='application/json')
        assert response.status_code == 404
        json_data = json.loads(response.data)
        assert json_data['error'] == 'not found'
    
    def test_delete_item_success(self, client):
        """Test deleting an item successfully."""
        # Create an item first
        data = {"name": "Item to Delete", "description": "Will be deleted"}
        create_response = client.post('/items', 
                                    data=json.dumps(data),
                                    content_type='application/json')
        item_id = json.loads(create_response.data)['id']
        
        # Delete the item
        response = client.delete(f'/items/{item_id}')
        assert response.status_code == 204
        assert response.data == b''
        
        # Verify it's gone
        get_response = client.get(f'/items/{item_id}')
        assert get_response.status_code == 404
    
    def test_delete_item_not_found(self, client):
        """Test deleting an item that doesn't exist."""
        response = client.delete('/items/999')
        assert response.status_code == 404
        json_data = json.loads(response.data)
        assert json_data['error'] == 'not found'

class TestAppConfiguration:
    """Test cases for application configuration."""
    
    def test_app_creation_default_db(self):
        """Test creating app with default database URL."""
        app = create_app()
        assert app is not None
        assert hasattr(app, 'session_factory')
    
    def test_app_creation_custom_db_url(self):
        """Test creating app with custom database URL."""
        app = create_app(db_url='sqlite:///test.db')
        assert app is not None
        assert hasattr(app, 'session_factory')
    
    def test_app_creation_with_engine(self):
        """Test creating app with provided engine."""
        engine = create_engine('sqlite:///:memory:', connect_args={"check_same_thread": False})
        app = create_app(engine=engine)
        assert app is not None
        assert hasattr(app, 'session_factory')
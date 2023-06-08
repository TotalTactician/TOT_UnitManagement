import json
from bson import ObjectId
from unittest import mock
from main import create_app
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

def test_getUnit(app):
    # Create a mock database and collection
    mock_db = {"units": {}}
    app.db = mock_db

    # Define a sample unit
    sample_unit = {"_id": ObjectId(), "name": "Test Unit"}

    # Add the sample unit to the mock collection
    mock_db["units"][str(sample_unit["_id"])] = sample_unit
    print(mock_db)
    # Make a request to the API endpoint
    response = app.test_client().get(f"/api/unit/{sample_unit['_id']}")

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the response data matches the sample unit
    print(response.data)
    assert json.loads(response.data) == json.loads(json.dumps(sample_unit, default=str))

    # Check that the find_one method was called with the correct argument
    assert "units" in mock_db
    assert str(sample_unit["_id"]) in mock_db["units"]
    assert mock_db["units"][str(sample_unit["_id"])] == sample_unit



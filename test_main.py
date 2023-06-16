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

def test_getUnit(app, mocker):

    # Define a sample unit
    sample_unit = {"_id": ObjectId("647f10601bf12007cc8b55c6"), "name": "Test Unit"}
    mocker.patch.object(app.db, "find_one", return_value=sample_unit)

    # Make a request to the API endpoint
    response = app.test_client().get(f"/api/unit/{sample_unit['_id']}")

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the response data matches the sample unit
    print(response.data)
    assert json.loads(response.data) == json.loads(json.dumps(sample_unit, default=str))



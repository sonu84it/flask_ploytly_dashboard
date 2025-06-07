import pytest
from app import app


def test_index_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"plotly-graph-div" in response.data

import pytest
import app


@pytest.fixture
def testmain():

    response = app.APP.test_client().get('/')
    assert response.status_code == 200

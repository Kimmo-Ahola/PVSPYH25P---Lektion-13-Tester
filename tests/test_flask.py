import pytest
from app import create_app
from config import TestConfig
from database import db as fake_db

@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig)

    with app.app_context():
        fake_db.create_all()

        from seeding import seed_database

        seed_database(fake_db)

    yield app # yield betyder att vi här skickar tillbaka objektet app

    # Här kan man lägga till teardown om det behövs

@pytest.fixture
def client(app):
    app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False
    )
    with app.test_client() as client:
        yield client


def test_create_customer_route(client):
    response = client.post(
        "/customers/create",
        data = {
            "name": "Alice",
            "email": "Smith",
            "address": "123 Main St",
            "city": "Townsville",
            "date_of_birth": "1991-08-04",
        },
        content_type="application/x-www-form-urlencoded"
    )
    
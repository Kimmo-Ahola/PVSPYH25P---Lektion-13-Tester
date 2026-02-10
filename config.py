import os

class Config:
    pass

# Dev environment
class DevConfig(Config):
    # We are missing SECRET_KEY .env
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE")
    DEBUG = True

# Dev environment
class TestConfig(Config):
    # Testing database can be in memory
    # sqlite:///memory
    # sqlite har ingen String(10)
    # sqlite tillåter strängar över 10 i längd
    # Så om ni skriver test på detta försvinner tyvärr valideringslogiken
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DATABASE')
    DEBUG = True
    TESTING = True
    # Disable CSRF för att fixa testning av WTForms
    # Denna ska annars ALLTID vara True
    WTF_CSRF_ENABLED = False

# Dev environment
class ProdConfig(Config):
    # Endast specifika personer får tillgång till denna
    # Ni som praktikanter får förmodligen inte det
    # För stor risk att det blir stora konsekvenser
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE")
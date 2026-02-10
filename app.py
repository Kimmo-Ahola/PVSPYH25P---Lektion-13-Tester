from typing import Type
from dotenv import load_dotenv

load_dotenv()  # This must be before the config class!!!
# Otherwise we do not have env values loaded properly

from config import Config, DevConfig


from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from routes.customer_route import customers_bp
from seeding import seed_database


# Application factory som skickar tillbaka ett app-objekt av typen Flask
# Man brukar ha 3 miljöer (minst)
# Local environment = på din dator
# Staging enviroment = lokalt på kontoret = Dev environment
# Testing environment = Helt frånkopplad. Oftast en in-memory-databas eller container med docker.
# Production environment = appen är live på nätet
def create_app(config_class: Type[Config] = DevConfig):
    app = Flask(__name__)

    # load configurations from config.py
    # config class comes from the parameter in create_app
    # DevConfig is the default config
    app.config.from_object(config_class)

    from database import db

    db.init_app(app)
    migrate = Migrate(app, db)

    # register customer routes
    app.register_blueprint(customers_bp)

    @app.route("/form")
    def example():
        return render_template("classic-form-example.html")

    @app.route("/")
    def home():
        return redirect(url_for("customers.get_all"))

    return app


if __name__ == "__main__":
    # We can use FLASK_DEBUG to set ProdEnvironment here if we want to.
    app = create_app(DevConfig)

    with app.app_context():
        from database import db

        seed_database(db)
    app.run(debug=True)

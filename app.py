import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from routes.customer_route import customers_bp
from database import db
from seeding import seed_database
import models


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DEVELOPMENT_DATABASE")
app.config["SECRET_KEY"] = "this-is-not-secret-please-use-env"

app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG", "0") == "1"
app.config["WTF_CSRF_ENABLED"] = not app.config["FLASK_DEBUG"]

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


if __name__ == "__main__":
    with app.app_context():
        seed_database(db)
    app.run(debug=True)

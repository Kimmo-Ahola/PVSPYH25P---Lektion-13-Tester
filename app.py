# introduction to flask-wtforms
# a way to improve forms with better security, built in validators etc.
# https://flask-wtf.readthedocs.io/en/1.2.x/

# pip install Flask-WTF
import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from routes.customer_route import customers_bp
from database import db
from seeding import seed_database
import models
load_dotenv()
app = Flask(__name__)

# Denna bör vara i .env istället
# Se till att ni har denna databas skapad innan ni kör appen
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://user:user123@localhost:3306/delete_me"
)
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
    # from flask import redirect, url_for
    # redirect = vi dirigerar om till en annan sida
    # url_for = vi bygger en länk dynamiskt.
    # customers i detta fall är namespace till vår blueprint
    # get_all är namnet på funktionen inuti customers namespace
    return redirect(url_for("customers.get_all"))


if __name__ == "__main__":
    with app.app_context():
        seed_database(db)
    app.run(debug=True)

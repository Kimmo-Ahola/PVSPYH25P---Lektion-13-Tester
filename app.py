from flask import Flask, render_template
from flask_migrate import Migrate
from routes.customer_route import customer_bp
from database import db
from seeding import seed_database
import models

app = Flask(__name__)

# Vi skippar .env i detta exempel. 
# Se till att ni har denna databas skapad innan ni kör appen
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://user:user123@localhost:3306/delete_me"
)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(customer_bp)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        seed_database(db)
    app.run(debug=True)

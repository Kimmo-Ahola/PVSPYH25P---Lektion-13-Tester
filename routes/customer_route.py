from flask import Blueprint, render_template, current_app, request
from database import db
from models.customer import Customer

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")


@customers_bp.route("/<int:id>")
def get(id: int):
    return ""


@customers_bp.route("/")
def get_all():
    customers = db.session.query(Customer).all()
    return render_template("customers/customers.html", customers=customers)


@customers_bp.route("/create")
def create():
    return ""


@customers_bp.route("/update/<int:id>")
def update(id: int):
    return ""


@customers_bp.route("/delete/<int:id>")
def delete(id: int):
    return ""

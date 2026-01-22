from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from database import db
from models.customer import Customer
from models.forms import CustomerCreateForm

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")


@customers_bp.route("/<int:id>")
def get(id: int):
    return ""


@customers_bp.route("/")
def get_all():
    customers = db.session.query(Customer).all()
    return render_template("customers/customers.html", customers=customers)


@customers_bp.route("/create", methods=["GET", "POST"])
def create():
    # Skapa formuläret för att skicka in det i vår template
    form = CustomerCreateForm()

    # Om metoden är post, då kollar vi alla validators.
    if form.validate_on_submit():

        # kom ihåg denna i er bankapp på alla unika kolumner!
        # if email exists in db: break

        form_data = {
            "name": form.name.data,
            "email": form.email.data,
            "address": form.address.data,
            "city": form.city.data,
            "date_of_birth": form.date_of_birth.data,
            "telephone": form.telephone.data,
            "secondary_address": form.secondary_address.data,
            "national_id": form.national_id.data,
        }
        try:
            new_customer = Customer(**form_data)
            db.session.add(new_customer)
            db.session.commit()
            # Vi är inte i jinja, så vi skippar {{}}
            # Flash används för att skapa tillfälliga flash-meddelanden som läggs inuti layout.html
            flash(message="Du skapade en kund!", category="success")
            return redirect(url_for("customers.get_all"))
        except Exception as e:
            print(e)

    return render_template("customers/create.html", form=form)


@customers_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id: int):
    my_customer = db.session.get(Customer, id)
    form = CustomerCreateForm(obj=my_customer)

    if form.validate_on_submit():
        form.populate_obj(my_customer)
        db.session.commit()
        flash("Kunden är uppdaterad", "success")
        return redirect(url_for("customers.get_all"))

    return render_template("customers/update.html", form=form)


@customers_bp.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id: int):
    if request.method == "POST":
        # Add soft delete, otherwise this will not work unless you delete account as well
        # you can also update the db to use delete-cascade
        # helst try except på denna också!
        customer = db.session.get(Customer, id)
        # db.session.delete(customer)
        # db.session.commit()
        flash("Kunden är raderad", "success")
        return redirect(url_for("customers.get_all"))
    return render_template("customers/delete.html", id=id)

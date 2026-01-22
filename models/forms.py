from datetime import date
from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DecimalField,
    HiddenField,
    IntegerField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Optional, Length, Regexp


def is_adult():
    from wtforms.validators import ValidationError
    from dateutil import relativedelta

    def _is_adult(form, field):
        if field.data is None:

            raise ValidationError("Date of birth is required")

        today = date.today()
        delta = relativedelta.relativedelta(today, field.data)

        if delta.years < 18:
            raise ValidationError("You must be at least 18 years old")

    return _is_adult


class AccountDepositForm(FlaskForm):
    receiving_account_id = HiddenField()
    amount = DecimalField()


class AccountWithdrawForm(FlaskForm):
    withdrawing_account_id = HiddenField()
    amount = DecimalField()


class AccountTransferForm(FlaskForm):
    withdrawing_account_id = HiddenField()
    receiving_account_id = HiddenField()
    amount = DecimalField()


class CustomerCreateForm(FlaskForm):
    # Fält som vi tar bort id, user_role
    name = StringField(
        label="Name",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Full Name"},
    )
    email = StringField(
        label="Email",
        validators=[DataRequired(), Length(min=1, max=255)],
        render_kw={"placeholder": "Full Name"},
    )
    address = StringField(
        label="Address",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Full Name"},
    )
    city = StringField(
        label="City",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Full Name"},
    )
    date_of_birth = DateField(
        label="Date of Birth",
        validators=[DataRequired(), is_adult()],
        render_kw={
            "placeholder": "YYYY-MM-DD",
            "format": "YYYY-MM-DD",
            "max": date.today().isoformat(),
        },
    )

    # Optional fields
    telephone = StringField(
        label="Telephone",
        validators=[
            Optional(),
            Length(min=1, max=20),
            Regexp(r"^\d+$", message="Must contain only numbers"),
        ],
        render_kw={"placeholder": "Full Name"},
    )
    secondary_address = StringField(
        label="Secondary Address",
        validators=[Optional(), Length(min=1, max=255)],
        render_kw={"placeholder": "Full Name"},
    )
    national_id = StringField(
        label="National Id",
        validators=[Optional(), Length(min=1, max=20)],
        render_kw={"placeholder": "Full Name"},
    )

    submit = SubmitField("Create Customer")

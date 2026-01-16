from datetime import date
from typing import Annotated, List, Optional
from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

str_255 = Annotated[str, mapped_column(db.String(255))]
str_100 = Annotated[str, mapped_column(db.String(100))]


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str_100]
    email: Mapped[str_255]
    address: Mapped[str_100]
    city: Mapped[str_100]
    date_of_birth: Mapped[date]
    # Optional fields
    telephone: Mapped[Optional[str]] = mapped_column(db.String(20), nullable=True)
    secondary_address: Mapped[Optional[str_255]] = mapped_column(nullable=True)
    national_id: Mapped[Optional[str]] = mapped_column(db.String(20), nullable=True)

    # Relationship
    # One user can have many accounts = list
    accounts: Mapped[List["Account"]] = relationship(back_populates="user")

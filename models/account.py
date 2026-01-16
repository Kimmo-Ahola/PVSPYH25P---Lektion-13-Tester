from decimal import Decimal
from database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DECIMAL

class Account(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[Decimal] = mapped_column(DECIMAL(12, 3))

    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))


    # Relationships
    # One account belongs to one user
    user: Mapped["User"] = relationship(back_populates="accounts")
import random
from faker import Faker

from models.account import Account
from models.user import User


def seed_database(db):
    if not db.session.query(User).first():
        print("Seeding!")
        min_amount = 0
        max_amount = 10**5  # 10^5
        users: list[User] = []
        fake = Faker("sv_SE")
        for _ in range(5):
            new_user = User(
                name=fake.name(),
                email=fake.unique.email(),
                address=fake.address(),
                city=fake.city(),
                date_of_birth=fake.date_of_birth(),
                accounts=[
                    Account(balance=random.randrange(min_amount, max_amount)),
                    Account(balance=random.randrange(min_amount, max_amount)),
                ],
            )

            users.append(new_user)
        db.session.add_all(users)
        db.session.commit()
    else:
        print("Seeding already done!")

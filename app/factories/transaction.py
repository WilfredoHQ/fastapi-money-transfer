import factory
from sqlalchemy import func

from app.api.deps import get_db
from app.models import Subsidiary, Transaction, User


class TransactionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Transaction
        sqlalchemy_session = next(get_db())
        sqlalchemy_session_persistence = "commit"

    code = factory.Faker("ean", length=8)
    transmitter = factory.Faker("name")
    receiver = factory.Faker("name")
    quantity = factory.Faker("pydecimal", right_digits=2, positive=True, max_value=50000)
    commission = factory.Faker("pydecimal", right_digits=2, positive=True, max_value=500)
    is_delivered = factory.Faker("pybool")


def generate_transactions(
    quantity: int = 50
):
    last_user_id = next(get_db()).query(func.max(User.id)).one()[0]
    last_subsidiary_id = next(get_db()).query(func.max(Subsidiary.id)).one()[0]

    if last_user_id and last_subsidiary_id:
        for _ in range(quantity):
            TransactionFactory(user_id=factory.Faker("random_int", min=1, max=last_user_id),
                               from_subsidiary_id=factory.Faker("random_int", min=1, max=last_subsidiary_id),
                               to_subsidiary_id=factory.Faker("random_int", min=1, max=last_subsidiary_id)
                               )

        print("Transactions have been generated")
    else:
        print("No registered users or subsidiaries")

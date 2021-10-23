import factory

from app.api.deps import get_db
from app.models import Subsidiary


class SubsidiaryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Subsidiary
        sqlalchemy_session = next(get_db())
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("sentence", nb_words=10)


def generate_subsidiaries(
    quantity: int = 10
):
    for _ in range(quantity):
        SubsidiaryFactory()

    print("Subsidiaries have been generated")

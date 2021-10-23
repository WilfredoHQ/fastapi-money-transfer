import factory

from app.api.deps import get_db
from app.core.security import get_password_hash
from app.models import User


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = next(get_db())
        sqlalchemy_get_or_create = ("email",)
        sqlalchemy_session_persistence = "commit"

    dni = factory.Faker("ean", length=8)
    full_name = factory.Faker("name")
    email = factory.Faker("ascii_email")
    hashed_password = get_password_hash("admin")
    is_active = factory.Faker("pybool")


def generate_users(
    quantity: int = 10
):
    for _ in range(quantity):
        UserFactory()

    print("Users have been generated")

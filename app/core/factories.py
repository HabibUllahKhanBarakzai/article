from factory.django import DjangoModelFactory
import factory
import random

from . import UserTypes
from .models import User


def retrieve_user_type():
    """This method will retrieve user type"""

    choices = [x[0] for x in UserTypes.CUSTOM_TYPES]
    return random.choice(choices)


class UserFactory(DjangoModelFactory):
    """Factory mock objects for user model"""

    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_joined = factory.Faker('date_time')
    email = factory.Faker('email')




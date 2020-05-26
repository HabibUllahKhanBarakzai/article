
from typing import Dict
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.status import HTTP_201_CREATED
from .models import (User, Writer, Editor)


class BaseRegisterView(APIView):
    """Base API to register The user, it can either be Writer or Publisher"""

    @classmethod
    def create_type(cls, user: User):
        """OverRide this method to either create Writer or Editor based
            on api, or use case"""
        pass

    @classmethod
    def create_serialized_user_object(cls, user: User) -> Dict:
        """Serialize User object """
        return {"email": user.email, "date_joined": user.date_joined}

    def post(self, request, *args, **kwargs):
        """Create the base User"""
        user = User.objects.create_user(**request.data)
        self.create_type(user)
        data = self.create_serialized_user_object(user)

        return Response(data=data,
                        status=HTTP_201_CREATED)


class WriterRegisterView(BaseRegisterView):
    """Register the Writer View"""

    @classmethod
    def create_type(cls, user: User):
        """Creating Writer object for user"""
        Writer.objects.create_type(user)


class EditorRegisterView(BaseRegisterView):
    """Register the Editor Api"""

    @classmethod
    def create_type(cls, user: User):
        """Creating Writer object for user"""
        Editor.objects.create_type(user)

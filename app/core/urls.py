from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path

from .views import WriterRegisterView, EditorRegisterView

auth_patterns = [
    path(r'token/obtain/', obtain_jwt_token),
    path(r'token/refresh/', refresh_jwt_token)
]

register_patterns = [
    path('writer/', WriterRegisterView.as_view(), name="register-writer"),
    path('editor/', EditorRegisterView.as_view(), name="register-editor"),

]
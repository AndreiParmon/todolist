from django.contrib import admin
from django.urls import path, include

from core.views import SignupView

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"), # имена нам потребуются позже, рекомендую всегда их проставлять!
]

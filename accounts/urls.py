from django.urls import path

from accounts.views import SignUpView

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    # path('login', LoginView.as_view()),
]
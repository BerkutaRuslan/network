from django.urls import path

from accounts.views import SignUpView, SignInView, UserActivityView

urlpatterns = [
    path('sign-up-request', SignUpView.as_view()),
    path('sign-in-request', SignInView.as_view()),
    path('activity', UserActivityView.as_view()),
]
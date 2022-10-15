from django.urls import path

from .views import RegistrationView, ActivationView, LoginView, LogoutView, ForgotPasswordView, ChangePasswordView


urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activation/',ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
]

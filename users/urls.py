from django.urls import path
from users.views import email_verification, profile, login, registration

app_name = "users"

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
]

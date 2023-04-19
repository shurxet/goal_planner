from django.urls import path
from bot import views


urlpatterns = [
    path('verify', views.UserVerificationView.as_view(), name='verify_user')
]

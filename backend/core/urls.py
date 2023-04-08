from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.user import\
    UserLoginView,\
    UserCreateView,\
    UserProfileView,\
    UserPasswordUpdateView

urlpatterns = [
    path("signup", UserCreateView.as_view(), name="signup"),
    path("login", UserLoginView.as_view(), name="login"),
    path("profile", UserProfileView.as_view(), name="profile "),
    path("update_password", UserPasswordUpdateView.as_view(), name="update_password"),


    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from core import models
from core import serializers
from django.contrib.auth import login, logout


class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserCreateSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = serializers.UserLoginSerializer

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> models.User:
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPasswordUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.UserPasswordUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

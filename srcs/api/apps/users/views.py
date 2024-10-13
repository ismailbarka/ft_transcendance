from rest_framework import generics
from .serializers import AuthUserSerializer, SignUpSerializer
from rest_framework.permissions import AllowAny
from .models import User

class   SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


class   AuthUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthUserSerializer

    def get_object(self):
        return self.request.user

class   ListUserView(generics.ListAPIView):
    serializer_class = AuthUserSerializer

    def get_queryset(self):
        return User.objects.all()


"""
/api/users/me
/api/users/{user_id}
"""
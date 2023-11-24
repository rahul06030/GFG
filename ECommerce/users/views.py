from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from .serializers import CustomerSerializer

class CustomerLoginView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        customer = authenticate(request, email=email, password=password)

        if customer:
            login(request, customer)
            token, created = Token.objects.get_or_create(user=customer)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomerLogoutView(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class CustomerRegistrationView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = serializer.save()
        customer.set_password(request.data.get('password'))
        customer.save()

        return Response({'message': 'Customer registered successfully'}, status=status.HTTP_201_CREATED)
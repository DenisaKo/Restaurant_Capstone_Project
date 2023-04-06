from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated


from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

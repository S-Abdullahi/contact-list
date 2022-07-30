from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from user_app.api.serializer import ContactSerializer
from user_app.models import Contact

from rest_framework import generics
from rest_framework import filters

# from rest_framework.permissions import IsAdminUser

class ContactList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']


class ContactInd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

    
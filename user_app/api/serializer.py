from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from user_app.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phoneNumber', 'email', 'address']
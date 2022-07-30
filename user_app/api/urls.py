from django.urls import path
from user_app.api.views import ContactList, ContactInd


urlpatterns = [
    path('contact/', ContactList.as_view(), name='contact'),
    path('addcontact/<int:pk>', ContactInd.as_view(), name='contact-detail'),
]
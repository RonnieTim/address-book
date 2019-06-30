from rest_framework.viewsets import ModelViewSet

from .models import Contacts
from .serializers import ContactsSerializer


class ContactsViewSet(ModelViewSet):
    """Contacts api endpoint for listing and adding, updating, deleting contacts."""
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

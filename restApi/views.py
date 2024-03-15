from rest_framework import viewsets
from .serializer import DeveloperSerializer
from .models import developer

# Create your views here.

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = developer.objects.all()
    serializer_class = DeveloperSerializer
from home.empserializer import Empserializer
from home.models import Emp
from rest_framework import viewsets
class Empviewset(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class=Empserializer
from rest_framework import generics
from .models import Building
from .serializers import BuildingSerializer
from .permissions import IsOwnerOrReadOnly

class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsOwnerOrReadOnly]
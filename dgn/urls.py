from django.urls import path
from .views import BuildingListCreateView, BuildingDetailView

urlpatterns = [
    path('', BuildingListCreateView.as_view(), name='building_list'),
    path('<int:pk>/', BuildingDetailView.as_view(), name='building_detail'),
]
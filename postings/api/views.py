

from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.response import Response

from postings.models import Food, Meals, Tasks
from .permissions import IsOwnerOrReadOnly
from .serializers import FoodSerializer, MealSerializer, TaskSerializer

class FoodAPIView(mixins.CreateModelMixin, generics.ListAPIView): 
    lookup_field            = 'pk' 
    serializer_class        = FoodSerializer
    

    def get_queryset(self):
        qs = Food.objects.all()
        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class MealAPIView(mixins.CreateModelMixin, generics.ListAPIView): 
    lookup_field            = 'pk' 
    serializer_class        = MealSerializer
    

    def get_queryset(self):
        qs = Meals.objects.all()
        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class TaskAPIView(generics.CreateAPIView):
    lookup_field            = 'pk'
    serializer_class        = TaskSerializer

    def perform_create(self, serializer):
         serializer.save()
         print (serializer.data)
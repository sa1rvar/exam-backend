from django.shortcuts import render
from rest_framework import  generics
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from project.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from app.models import Food, Category
from app.serializer import FoodSerializersRetr, FoodSerializers, CategorySerializers, CategorySerializersRetr




class ProjectCreate(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsAuthenticated,)

class ProjectList(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers


class ProjectUpdate(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsOwnerOrReadOnly,)


class ProjectUpdateRetrieve(generics.RetrieveUpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializersRetr
    permission_classes = (IsAdminUser,)

class ProjectDelete(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    permission_classes = (IsAdminOrReadOnly,)

class ProjectFoodList(APIView):
    def get(self,request):
        list_person = Category.objects.all()
        return Response({"Persons": FoodSerializersRetr(list_person, many=True).data})

class ProjectCreateCat(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = (IsAuthenticated,)

class ProjectListCat(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProjectUpdateCat(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = (IsOwnerOrReadOnly,)

class ProjectDelCat(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = (IsAdminOrReadOnly,)


class CategoryList(APIView):
    def get(self,request):
        list_person = Category.objects.all()
        return Response({"Persons": CategorySerializersRetr(list_person, many=True).data})

































































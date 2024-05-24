# from django.shortcuts import render
# from django.http import HttpResponse
from django.db.models.deletion import RestrictedError, ProtectedError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .serializers import VacationSerializer, CategorySerializer
from .models import Vacation, Category


@api_view(['GET'])
def vacations_list(request):

    if request.method == 'GET':
        vacations = Vacation.objects.select_related('category', 'author')
        serializer = VacationSerializer(vacations, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def categories_list(request):
    
    if request.method == 'GET':
        categories = Category.objects
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)  
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):

    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            category.delete()
        except RestrictedError as error:
            restricted_elements = [
                {"id": restricted_object.pk, "type": str(restricted_object.__class__.__name__)}
                for restricted_object in error.restricted_objects
            ]
            response_data = {"detail" : str(error), "restricted_elements": restricted_elements}
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

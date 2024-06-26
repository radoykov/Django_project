from django.db.models.deletion import RestrictedError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import VacationSerializer, CategorySerializer
from .models import Vacation, Category
from .custom_permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def vacations_list(request):

    if request.method == 'GET':
        category_from_query = request.query_params.get('category')
        if category_from_query == None:
            vacations = Vacation.objects.select_related('category', 'author').all()
        else:
            vacations = Vacation.objects.filter(category_id = category_from_query).select_related('category', 'author').all()
            
        serializer = VacationSerializer(vacations, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VacationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET', 'POST'])
@permission_classes([IsAdminOrReadOnly])
def categories_list(request):
    
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)  
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminOrReadOnly])
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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthorOrReadOnly])
def vacation_detail(request, pk):

    try:
        vacation = Vacation.objects.get(pk=pk)
    except Vacation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacationSerializer(vacation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacationSerializer(vacation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = VacationSerializer(vacation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vacation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
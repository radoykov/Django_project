from django.db.models.deletion import RestrictedError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .serializers import CommentSerializer
from .models import Vacation, Comment

@api_view(['GET', 'POST'])
def all_comments_for_vacation(request, vacation_id):
    
    if not Vacation.objects.filter(pk=vacation_id).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comments = Comment.objects.filter(vacation=vacation_id).all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, vacation_id=vacation_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, vacation_id, comment_id):

    try:
        comment = Comment.objects.filter(vacation_id=vacation_id).get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save(vacation_id=vacation_id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
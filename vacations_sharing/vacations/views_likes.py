from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .models import Vacation

@api_view(['GET'])
def get_likes(request, vacation_id):
    try:
        vacation = Vacation.objects.get(id=vacation_id)
    except Vacation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    liked_users = vacation.likes.values_list('username', flat=True).all()
    return Response({'count': liked_users.count(), 'users': liked_users})

@api_view(['POST'])
def like_vacation(request, vacation_id):
    try:
        vacation = Vacation.objects.get(pk=vacation_id)
    except Vacation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if user in vacation.likes.all():
        return Response({"detail": "User already liked this vacation!"})
    
    vacation.likes.add(user)
    vacation.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def dislike_vacation(request, vacation_id):
    try:
        vacation = Vacation.objects.get(pk=vacation_id)
    except Vacation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if user in vacation.likes.all():
        vacation.likes.remove(user)
        vacation.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    return Response({"detail": "User hasn't liked this vacation!"})
    
    
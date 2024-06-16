from rest_framework import serializers
from vacations.models import Vacation, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']

class VacationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    #category = serializers.ReadOnlyField(source='category.name')
    #category = CategorySerializer()
    
    class Meta:
        model = Vacation
        fields = ['id', 'title', 'description', 'picture_url', 'start_date', 'end_date', 'category', 'author', 'date_created']
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    vacation =serializers.ReadOnlyField(source='vacation.title')
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'vacation', 'author', 'date_created']


    
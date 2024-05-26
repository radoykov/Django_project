from rest_framework import serializers
from vacations.models import Vacation, Category

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

    
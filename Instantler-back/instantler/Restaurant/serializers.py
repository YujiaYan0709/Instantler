from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','user', 'address', 'city', 'state', 'photo_url','name', 'phone_num', 'price','ratings_count','rating')

class RestaurantCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCat
        fields = ('id','restaurant', 'title')  # user is the User's id

'''
class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','restaurant', 'user', 'description', 'ratings', 'date')
'''

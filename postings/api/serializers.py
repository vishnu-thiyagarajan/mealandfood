from rest_framework import serializers
from postings.api.solution import get_matching_meals
from postings.models import Food, Meals, Tasks

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'food_id',
            'food_name',
        ]
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = [
            'meals_id',
            'foods',
        ]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'Meals_and_Foods',
            ]

    def validate_Meals_and_Foods(self, value):
        meal_data = []
        meals = Meals.objects.all()
        list_food = [v.food_id for v in value]
        print(meals)
        for item in meals:
            food_dct = []
            for food in item.foods.all():
                food_dct.append({'food_id':food.food_id,'food_name':food.food_name})
            meal_data.append({'meal_id':item.meals_id,'foods':food_dct})
        ans = get_matching_meals(meal_data=meal_data, food_ids=list_food)
        return ans
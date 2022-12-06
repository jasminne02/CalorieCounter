from django.contrib.auth.models import Group

from CalorieCounter.calorie_counter.views import calculate_eaten_carbs, calculate_eaten_protein, \
    calculate_eaten_fats, calculate_eaten_calories


def is_user_in_group(request, value):
    try:
        return request.user.groups.get(name=value)
    except Group.DoesNotExist:
        return None


def add_food_to_daily_data(daily_data, food):
    for f in food:
        daily_data.calories_eaten += calculate_eaten_calories(f, 100)
        daily_data.fats_grams_per_day += calculate_eaten_fats(f, 100)
        daily_data.carbs_grams_per_day += calculate_eaten_carbs(f, 100)
        daily_data.proteins_grams_per_day += calculate_eaten_protein(f, 100)


def add_meal_to_daily_data(daily_data, meals):
    for meal in meals:
        daily_data.calories_eaten += calculate_eaten_calories(meal, meal.grams)
        daily_data.fats_grams_per_day += calculate_eaten_fats(meal, meal.grams)
        daily_data.carbs_grams_per_day += calculate_eaten_carbs(meal, meal.grams)
        daily_data.proteins_grams_per_day += calculate_eaten_protein(meal, meal.grams)

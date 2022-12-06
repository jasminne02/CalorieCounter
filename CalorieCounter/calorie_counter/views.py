from django.shortcuts import render, redirect

from CalorieCounter.core.models import FoodPlan
from CalorieCounter.calorie_counter.forms import SearchFoodForm, SearchActivityForm, AddFoodForm, AddActivityForm
from CalorieCounter.calorie_counter.functionality import *


def show_calorie_counter(request):
    user = CustomUser.objects.get(username=request.user.username)
    daily_data = get_daily_data(user)
    food_search_form = SearchFoodForm()
    activity_search_form = SearchActivityForm()

    food_searched_object = None
    activity_searched_object = None

    if request.method == 'POST':
        if 'search-food' in request.POST:
            food_search_form = SearchFoodForm(request.POST)
            if food_search_form.is_valid():
                searched = food_search_form.cleaned_data['name']
                food_searched_object = food_search_query(searched)
        elif 'search-activity' in request.POST:
            activity_search_form = SearchActivityForm(request.POST)
            if activity_search_form.is_valid():
                searched = activity_search_form.cleaned_data['name']
                activity_searched_object = activity_search_query(searched)

    context = {
        'user': user,
        'left_calories': calculate_left_calories(user, daily_data),
        'daily_data': daily_data,
        'food_search_form': food_search_form,
        'activity_search_form': activity_search_form,
        'food_searched_object': food_searched_object,
        'activity_searched_object': activity_searched_object,
        'weekly_data': get_weekly_data(user),
    }

    return render(request, 'calorie_counter/calorie_counter.html', context)


def add_activity(request, pk):
    user = CustomUser.objects.get(username=request.user.username)
    activity_object = Exercise.objects.get(pk=pk)
    form = AddActivityForm()

    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            daily_data = get_daily_data(user)
            activity_object.daily_data_pk.add(daily_data.pk)
            activity_object.save()

            active_minutes = form.cleaned_data['active_minutes']
            daily_data.calories_burnt += calculate_burnt_calories(user=user, active_minutes=active_minutes,
                                                                  activity=activity_object)
            if form.cleaned_data['add_burnt_to_total']:
                daily_data.total_calories += daily_data.calories_burnt
            daily_data.save()
            return redirect('calorie counter')

    context = {
        'form': form,
        'activity_name': activity_object.name,
    }

    return render(request, 'calorie_counter/add_activity.html', context)


def add_food(request, name):
    user = CustomUser.objects.get(username=request.user.username)
    food_object = food_search_query(name)
    form = AddFoodForm()

    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            daily_data = get_daily_data(user)
            food_object.daily_data_pk.add(daily_data.pk)
            food_object.save()

            grams = form.cleaned_data['grams']
            daily_data.calories_eaten += calculate_eaten_calories(food_object, grams)
            daily_data.fats_grams_per_day += calculate_eaten_fats(food_object, grams)
            daily_data.proteins_grams_per_day += calculate_eaten_protein(food_object, grams)
            daily_data.carbs_grams_per_day += calculate_eaten_carbs(food_object, grams)
            daily_data.save()
            return redirect('calorie counter')

    context = {
        'form': form,
        'food_name': food_object.name,
    }

    return render(request, 'calorie_counter/add_food.html', context)


def today_details(request):
    user = CustomUser.objects.get(username=request.user.username)
    daily_data = get_daily_data(user)

    context = {
        'daily_data': daily_data,
        'activities': Exercise.objects.filter(daily_data_pk=daily_data.pk),
        'meals': Meal.objects.filter(daily_data_pk=daily_data.pk),
        'food': Food.objects.filter(daily_data_pk=daily_data.pk),
        'food_plans': FoodPlan.objects.filter(daily_data_pk=daily_data.pk),
    }

    return render(request, 'calorie_counter/today_details.html', context)

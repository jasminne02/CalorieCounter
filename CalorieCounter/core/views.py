from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from CalorieCounter.calorie_counter.functionality import get_daily_data
from CalorieCounter.core.forms import MotivationsCreateForm
from CalorieCounter.core.models import FoodPlan, Motivation
from CalorieCounter.accounts.models import CustomUser
from CalorieCounter.core.functionality import *


def show_homepage(request):
    context = {
        'motivations': Motivation.objects.all()[:3],
        'motivation_group': is_user_in_group(request, 'Motivations')
    }
    return render(request, 'core/home.html', context)


def show_about_page(request):
    return render(request, 'core/about.html')


def add_plan_for_the_day(request, pk):
    user = CustomUser.objects.get(username=request.user.username)
    food_plan = FoodPlan.objects.get(pk=pk)
    daily_data = get_daily_data(user)
    food_plan.daily_data_pk.add(daily_data.pk)
    food_plan.save()

    food = food_plan.food.all()
    meals = food_plan.meals.all()
    add_food_to_daily_data(daily_data, food)
    add_meal_to_daily_data(daily_data, meals)
    daily_data.save()

    return redirect('calorie counter')


class FoodPlansView(views.ListView):
    queryset = FoodPlan.objects.all()
    template_name = 'core/food_plans.html'


class FoodPlanDetailsView(views.DetailView):
    model = FoodPlan
    template_name = 'core/food_details.html'

    def get_context_data(self, **kwargs):
        context = super(FoodPlanDetailsView, self).get_context_data(**kwargs)

        context['meals'] = self.object.meals.all()
        context['food'] = self.object.food.all()
        return context


class AddMotivationView(views.CreateView):
    model = Motivation
    form_class = MotivationsCreateForm
    template_name = 'account/add_motivations.html'
    success_url = reverse_lazy('motivations')


class MotivationsView(views.ListView):
    queryset = Motivation.objects.all()
    template_name = 'core/all_motivations.html'

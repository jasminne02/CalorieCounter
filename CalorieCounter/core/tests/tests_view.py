from datetime import datetime

from django.test import TestCase, Client
from django.test.client import RequestFactory

from CalorieCounter.accounts.models import CustomUser
from CalorieCounter.calorie_counter.functionality import create_daily_data, get_daily_data
from CalorieCounter.calorie_counter.models import DailyData
from CalorieCounter.core.models import FoodPlan, Meal
from CalorieCounter.core.views import add_plan_for_the_day


class AddPlanForTheDayTest(TestCase):
    def setUp(self):
        self.plan = FoodPlan(
            id=192,
            name='Plan',
            image_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.healthline.com',
        )

        self.meal = Meal(
            id=422,
            name='Meal',
            calories=412,
            grams=234,
            fats_grams=32,
            protein_grams=25,
            carbs_grams=65
        )

        self.user = CustomUser(
            username='user',
            password='1234hello',
            birthday='1999-11-23',
            gender='Male',
            height='189',
            weight=92,
        )

        self.user.save()

        self.meal.save()

        self.plan.full_clean()
        self.plan.save()

        self.plan.meals.add(self.meal)
        self.plan.save()

        create_daily_data(self.user)

        self.factory = RequestFactory()
        self.request = self.factory.get(f'/food-plan-details/{self.plan.pk}/add-for-the-day/')

    def test_daily_data__expect_meal_added(self):
        request = self.request
        request.user = Client()
        request.user.username = 'user'
        add_plan_for_the_day(request, self.plan.pk)

        daily_data = get_daily_data(self.user)

        self.assertEquals(self.plan.calories, daily_data.calories_eaten)
        self.assertEquals(self.plan.protein_grams, daily_data.proteins_grams_per_day)
        self.assertEquals(self.plan.fats_grams, daily_data.fats_grams_per_day)
        self.assertEquals(self.plan.carbs_grams, daily_data.carbs_grams_per_day)

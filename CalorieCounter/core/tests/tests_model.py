from django.test import TestCase

from CalorieCounter.core.models import FoodPlan, Meal


class FoodPlanModelTests(TestCase):

    def setUp(self):
        self.food_plan = FoodPlan(
            id=1092,
            name='Plan',
            image_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.healthline.com',
        )

        self.meal = Meal(
            id=4322,
            name='Meal',
            calories=412,
            grams=234,
            fats_grams=32,
            protein_grams=25,
            carbs_grams=65
        )

        self.meal.save()

        self.food_plan.full_clean()
        self.food_plan.save()

        self.food_plan.meals.add(self.meal)
        self.food_plan.save()

    def test_food_plan_calories_property__expect_correct_result(self):
        self.assertEquals(self.food_plan.calories, self.meal.calories)

    def test_food_plan_grams_property__expect_correct_result(self):
        self.assertEquals(self.food_plan.grams, self.meal.grams)

    def test_food_plan_fats_grams_property__expect_correct_result(self):
        self.assertEquals(self.food_plan.fats_grams, self.meal.fats_grams)

    def test_food_plan_protein_grams_property__expect_correct_result(self):
        self.assertEquals(self.food_plan.protein_grams, self.meal.protein_grams)

    def test_food_plan_carbs_grams_property__expect_correct_result(self):
        self.assertEquals(self.food_plan.carbs_grams, self.meal.carbs_grams)

import datetime
from calendar import monthrange


from CalorieCounter.accounts.models import CustomUser
from CalorieCounter.core.models import Food, Meal, Exercise
from CalorieCounter.calorie_counter.models import DailyData


def get_weekly_data(user):
    try:
        today = datetime.date.today()
        if today.day - 7 > 0:
            return DailyData.objects. \
                filter(user_id=user.id,
                       date__lte=today,
                       date__gt=datetime.date(today.year, today.month, today.day - 7)) \
                .order_by('date')

        previous_month = today.month - 1
        year = today.year if previous_month > 1 else today.year - 1
        left_days_count = 7 - today.day
        total_days_previous_month = monthrange(today.year, previous_month)[1]

        data_current_month = DailyData.objects. \
            filter(user_id=user.id,
                   date__lte=today,
                   date__gt=datetime.date(today.year, today.month, today.day - today.day + 1)) \
            .order_by('date')

        data_previous_month = DailyData.objects. \
            filter(user_id=user.id,
                   date__lte=today,
                   date__gt=datetime.date(year, previous_month,  total_days_previous_month - left_days_count)) \
            .order_by('date')
        return data_current_month | data_previous_month
    except DailyData.DoesNotExist:
        return None


def get_daily_data(user):
    try:
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        return DailyData.objects.get(user_id=user.id, date__range=(today_min, today_max))
    except DailyData.DoesNotExist:
        create_daily_data(user)
        return None


def create_daily_data(user):
    daily_data = DailyData.objects.create(date=datetime.date.today(), user_id=user)
    daily_data.total_calories = user.calories_per_day
    daily_data.calories_eaten = 0
    daily_data.calories_burnt = 0
    daily_data.carbs_grams_per_day = 0
    daily_data.proteins_grams_per_day = 0
    daily_data.fats_grams_per_day = 0
    daily_data.save()


def calculate_left_calories(user, daily_data):
    if daily_data:
        return daily_data.total_calories - daily_data.calories_eaten
    else:
        return user.calories_per_day


def calculate_eaten_calories(food, quantity):
    calories_per_gram = food.calories / food.grams
    return calories_per_gram * quantity


def calculate_eaten_fats(food, quantity):
    fats_per_gram = food.fats_grams / food.grams
    return fats_per_gram * quantity


def calculate_eaten_protein(food, quantity):
    protein_per_gram = food.protein_grams / food.grams
    return protein_per_gram * quantity


def calculate_eaten_carbs(food, quantity):
    carbs_per_gram = food.carbs_grams / food.grams
    return carbs_per_gram * quantity


def calculate_burnt_calories(user: CustomUser, activity: Exercise, active_minutes: int):
    return active_minutes * (activity.metabolic_equivalent * 3.5 * user.weight) / 200


def food_search_query(searched):
    try:
        return Food.objects.get(name=searched)
    except Food.DoesNotExist:
        searched = Meal.objects.filter(name__icontains=searched)
        if searched.count() > 0:
            return searched.first()
        else:
            return 'No search results'


def get_food_or_meal_by_name(name):
    try:
        searched = Food.objects.get(name=name)
        if searched is not None:
            return searched
    except Food.DoesNotExist:
        try:
            searched = Meal.objects.get(name=name)
            if searched is not None:
                return searched
        except Meal.DoesNotExist:
            return None


def activity_search_query(searched):
    searched = Exercise.objects.filter(name__icontains=searched)
    if searched.count() > 0:
        return searched.first()
    else:
        return 'No search results'

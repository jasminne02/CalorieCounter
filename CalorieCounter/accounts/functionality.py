def set_user_info(user):
    set_user_calories_per_day(user)
    set_user_fats_per_day(user)
    set_user_protein_per_day(user)
    set_user_carbs_per_day(user)
    user.save(update_fields=('calories_per_day', 'fats_grams_per_day', 'proteins_grams_per_day', 'carbs_grams_per_day'))


def set_user_calories_per_day(user):
    """ Revised Harris-Benedict Equation """
    if user.gender == 'Male':
        """ 66.47 + (13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years) """
        user.calories_per_day = 66.47 + (13.75 * user.weight) + (5.003 * user.height) - (6.755 * user.age)
    elif user.gender == 'Female':
        """ 655.1 + (9.563 x weight in kg) + (1.850 x height in cm) - (4.676 x age in years) """
        user.calories_per_day = 655.1 + (9.563 * user.weight) + (1.850 * user.height) - (4.676 * user.age)


def set_user_fats_per_day(user):
    """ 30% of total calorie intake should come from fats. Each gram of fat is 'worth' 9 calories """
    user.fats_grams_per_day = user.calories_per_day * 0.30 / 9


def set_user_protein_per_day(user):
    """ Around 20% of total calorie intake should come from proteins. Protein has four calories per gram """
    user.proteins_grams_per_day = user.calories_per_day * 0.20 / 4


def set_user_carbs_per_day(user):
    """ Around 50% of total calorie intake should come from carbs. Carbohydrates have four calories per gram """
    user.carbs_grams_per_day = user.calories_per_day * 0.5 / 4


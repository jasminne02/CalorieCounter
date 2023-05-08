import requests


class FoodAPIRequest:
    APP_ID = 'c405b5a'
    APP_KEY = '005749eb269bf8d49991da4fd1e3953d'
    API_URL = 'https://api.edamam.com/api/food-database/v2/parser?app_id={}8&app_key={}&ingr={}'

    @classmethod
    def get_request(cls, ingredients: str):
        ingredients = ingredients.replace(' ', '-')
        response = requests.get(FoodAPIRequest.API_URL.format(FoodAPIRequest.APP_ID, FoodAPIRequest.APP_KEY,
                                                              ingredients))
        if response.status_code == requests.codes.ok:
            return response.json()

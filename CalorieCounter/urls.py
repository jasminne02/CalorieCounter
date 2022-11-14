from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CalorieCounter.core.urls')),
    path('account/', include('CalorieCounter.accounts.urls')),
    path('calorie-counter/', include('CalorieCounter.calorie_counter.urls')),
]

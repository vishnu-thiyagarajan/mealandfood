from django.conf.urls import url


from .views import FoodAPIView, MealAPIView, TaskAPIView

urlpatterns = [
    url(r'^food/$', FoodAPIView.as_view(), name='food'),
    url(r'^meal/$', MealAPIView.as_view(), name='meal'),
    url(r'^task/$', TaskAPIView.as_view(), name='task'),
]   
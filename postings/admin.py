from django.contrib import admin


from .models import Food,Meals,Tasks

admin.site.register(Food)
admin.site.register(Meals)
admin.site.register(Tasks)
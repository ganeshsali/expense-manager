from django.contrib import admin
from .models import User, Balance, Category, Data

admin.site.register(User)
admin.site.register(Balance)
admin.site.register(Category)
admin.site.register(Data)



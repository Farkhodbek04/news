from django.contrib import admin
from .models import (
    Category, 
    Region,
    Item,
    Form
)

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Item)
admin.site.register(Form)
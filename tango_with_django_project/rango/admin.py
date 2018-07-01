from django.contrib import admin
from rango.models import Page,Category
#task
from rango.models import UserProfile
# Register your models here.
admin.site.register(Page)
admin.site.register(Category)

#task
admin.site.register(UserProfile)
from django.contrib import admin
from .models import Agent, Lead, User, Item, Instance_Item
# Register your models here.
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Instance_Item)

from django.contrib import admin
from fighters.models import Fighter

class ListFighters(admin.ModelAdmin):
    list_display = ("id","name","description")
    list_display_links = ("id","name")
    search_fields = ("name",)

admin.site.register(Fighter,ListFighters)
# Register your models here.

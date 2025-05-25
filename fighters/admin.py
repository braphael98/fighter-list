from django.contrib import admin
from fighters.models import Fighter

class ListFighters(admin.ModelAdmin):
    list_display = ("id","name","description","published")
    list_display_links = ("id","name")
    search_fields = ("name",)
    list_filter = ("difficulty_level",)
    list_editable =("published",)
    list_per_page = 10;


admin.site.register(Fighter,ListFighters)
# Register your models here.

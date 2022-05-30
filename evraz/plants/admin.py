from django.contrib import admin

from plants.models import Plant, PlantObject, ImportPlantsToggle


class PlantObjectInline(admin.TabularInline):
    model = PlantObject


class PlantAdmin(admin.ModelAdmin):
    model = Plant
    list_display = ['date', 'weight', 'status', 'unload_date']
    inlines = [PlantObjectInline]


admin.site.register(Plant, PlantAdmin)
admin.site.register(PlantObject)
admin.site.register(ImportPlantsToggle)

from django.contrib import admin
from .models import Area,CarDealer,Vehicles
# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Area,AreaAdmin)

class DealerAdmin(admin.ModelAdmin):
    pass
admin.site.register(CarDealer, DealerAdmin)

class VehicleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vehicles, VehicleAdmin)


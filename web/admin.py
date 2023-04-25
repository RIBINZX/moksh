from django.contrib import admin
from .models import Service,Gallery,Package
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        (' right', {
            'fields': ('title', 'image', 'sub_head', 'detail'),
        }),
        (' left', {
            'fields': ('title2', 'image2', 'sub_head2', 'detail2'),
        }),
    )

admin.site.register(Service, ServiceAdmin)

admin.site.register(Gallery)
# admin.site.register(Package)
class PackageAdmin(admin.ModelAdmin):
    fieldsets = (
        (' right', {
            'fields': ('title', 'image', 'sub_head', 'detail'),
        }),
        (' left', {
            'fields': ('title2', 'image2', 'sub_head2', 'detail2'),
        }),
    )

admin.site.register(Package, PackageAdmin)
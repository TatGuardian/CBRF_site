from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'typ', 'description', 'owner', 'image')
    search_fields = ('name',)
    list_filter = ('typ',)
    empty_value_display = '-пусто-'


admin.site.register(Company, CompanyAdmin)

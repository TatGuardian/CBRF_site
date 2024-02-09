from django.contrib import admin
from . import models as md

admin.site.register(md.Organisation)
admin.site.register(md.OrganisationType)
admin.site.register(md.Region)
admin.site.register(md.City)
admin.site.register(md.Product)
admin.site.register(md.ProductClass)
admin.site.register(md.ProductType)
admin.site.register(md.Filial)

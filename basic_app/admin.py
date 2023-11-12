from django.contrib import admin

from basic_app.models import Viloyat, Tuman, Stansiya, Osimlik, Hashorot, DataHashorot,data

# Register your models here.
admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Stansiya)
admin.site.register(Osimlik)
admin.site.register(Hashorot)
admin.site.register(DataHashorot)
admin.site.register(data)

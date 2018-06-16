from django.contrib import admin

from .models import *


class KrajAdmin(admin.ModelAdmin):
    fields = ['nazwa']


class KrajsInLine(admin.ModelAdmin):
    model = Adres_zamieszkania


class AdresAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['ulica', 'miejscowosc', ]}),
        ('Szczegóły', {'fields': ['numerBudynku', 'numerLokalu']}),
        (None, {'fields': ['kodPocztowy', 'kraj']}),
    ]


class KandydatAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    fields = ['osoba', 'wybor']
    # fields = ['osoba', 'wybor', 'votes']
=======
    fields = ['osoba', 'wybor', 'votes']
>>>>>>> 1ec22281e90e778e47a77d517b63d751a9262b46


admin.site.register(Kraj, KrajAdmin)
admin.site.register(Adres_zamieszkania, AdresAdmin)
admin.site.register(Osoba)
admin.site.register(Kryterium)
admin.site.register(Wybor)
admin.site.register(Kandydat, KandydatAdmin)
admin.site.register(Uprawniony)
admin.site.register(Oddany_glos)

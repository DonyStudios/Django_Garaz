from django.contrib import admin
from .models import Ridic, Vozidlo, Motor, Brzdy, Pneu, Odpruzeni

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Ridic)
admin.site.register(Vozidlo)
admin.site.register(Motor)
admin.site.register(Brzdy)
admin.site.register(Pneu)
admin.site.register(Odpruzeni)
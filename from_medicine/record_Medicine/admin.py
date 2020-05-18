from django.contrib import admin
from .models import Category, Product,Record
from noti_Prescription.models import Prescription
from reminder.models import remider
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'expirationDate',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'takingDate',)


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(remider)
class RemiderAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Ebook, Review

# Register your models here.
@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
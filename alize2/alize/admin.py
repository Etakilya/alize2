from django.contrib import admin
from .models import Pizza, Category, Steak, Salad, Comment
admin.site.register(Pizza)
admin.site.register(Category)
admin.site.register(Steak)
admin.site.register(Salad)
admin.site.register(Comment)
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')
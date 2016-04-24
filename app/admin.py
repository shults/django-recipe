from django.contrib import admin
from app.models import Category, Recipe, Step

class StepInline(admin.TabularInline):
    model = Step

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('full_title', 'created_at', 'published')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_full_title', 'created_at')
    inlines = [StepInline, ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

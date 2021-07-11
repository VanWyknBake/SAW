from django.contrib import admin
from .models import Home, About, News, Profile, Category, Skills, Portfolio, Category2, Skills2


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

# Skills


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)

# news


admin.site.register(News)

#SQUADS


class SkillsInline2(admin.TabularInline):
    model = Skills2
    extra = 2


@admin.register(Category2)
class CategoryAdmin2(admin.ModelAdmin):
    inlines = [
        SkillsInline2,
    ]



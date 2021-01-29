from django.contrib import admin

# Register your models here.
from .models import Movie, MovieImage

class MovieImageAdmin(admin.StackedInline):
    model=MovieImage

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines=[MovieImageAdmin]

    class Meta:
        model=Movie

@admin.register(MovieImage)
class MovieImageAdmin(admin.ModelAdmin):
    pass

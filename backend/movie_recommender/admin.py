from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'genre', 'director', 'year', 'rating','description')
    
admin.site.register(Movie, MovieAdmin)  
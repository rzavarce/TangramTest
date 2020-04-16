from django.contrib import admin

from .models import Article


class ArticlesAdmin(admin.ModelAdmin):

    list_display = ('art_title', 'art_content', 'art_status',)
    list_filter = ('art_title', 'art_status',)
    ordering = ('art_created_date',)
    search_fields = ('art_title',)    
	

admin.site.register(Article, ArticlesAdmin)



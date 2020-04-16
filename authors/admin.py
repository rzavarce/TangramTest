from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('aut_name', 'aut_email', 'aut_status', 'aut_creator')
    list_filter = ('aut_name', 'aut_email', 'aut_status',)
    ordering = ('aut_created_date',)
    search_fields = ('aut_name',)    
	

admin.site.register(Author, AuthorAdmin)



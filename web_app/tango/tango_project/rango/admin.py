from django.contrib import admin
from rango.models import Category, Page
#from rango.models import UserProfile
# Register your models here.

#admin.site.register(Page, PageAdmin)

# Create your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')


admin.site.register(Category)
#admin.site.register(Page, PageAdmin)
admin.site.register(Page)
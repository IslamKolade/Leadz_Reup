from django.contrib import admin
from .models import Leadz_Reup, Contact_Form_Submission
# Register your models here.
class Contact_Filter(admin.ModelAdmin): 
    search_fields = ('name',)
    #list_filter = ('user_type','form_purpose', 'free_quote')


admin.site.register(Leadz_Reup)
admin.site.register(Contact_Form_Submission, Contact_Filter)

admin.site.site_header = 'Leadz Reup Admin'
admin.site.site_title = 'Leadz Reup Admin Panel'
admin.site.index_title = 'Welcome to Leadz Reup Admin'
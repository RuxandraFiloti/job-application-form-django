from django.contrib import admin
from .models import Form

#to create a super user, run the command: python manage.py createsuperuser
#super user -> username: adda, email: adaflori0207@gmail.com password: Python2025!
#access the admin interface at: http://linkofthewebsite/admin

# Register your models here.

#this class is used to customize the admin interface for the Form model
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("first_name", ) #asc; for desc add a '-' before the field name
    readonly_fields = ("occupation", )

admin.site.register(Form, FormAdmin)
from django.contrib import admin
from .models import Post


@admin.register(Post)

class Studentadmin(admin.ModelAdmin):
    list_display= ['id','Author_Name','Author_id','Book_Name']
# Register your models here.

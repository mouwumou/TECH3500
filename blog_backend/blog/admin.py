from django.contrib import admin
from .models import Blog,BlogType

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'img', 'blog_type', 'author','created_time','last_updated_time')

from django.contrib import admin
from posts.models import BlogPost

# Register your models here. to see the model on the screen

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated",)
    list_editable = ("published", "created_on",)

# show model BlogPost on interface Admin
admin.site.register(BlogPost, BlogPostAdmin)
from django.contrib import admin
from .models import BlogPost, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('user', 'body')
    readonly_fields = ('user', 'body')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'id', )
    list_filter = ('user', )
    search_fields = ('title', 'user__email', 'user__first_name', 'user__last_name')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'post', 'parent' , 'id', )
    list_filter = ('user', 'post', 'parent')
    search_fields = ('body', 'user__email', 'user__first_name', 'user__last_name')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)

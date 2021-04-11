from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    readonly_fields = ('show_image',)
    list_filter = ('status', 'published', 'author', 'created')
    raw_id_fields = ('author', )
    date_hierarchy = 'published'
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def show_image(self, obj):
        return obj.view_image
    
    show_image.short_description = 'Imagem cadastrada'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'published',)
    list_filter = ('name', 'created', 'published',)
    date_hierarchy = 'published'
    search_fields = ('name',)


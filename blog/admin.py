from django.contrib import admin
from .models import Category, Post

# Category Actions
@admin.action(description="Seçili kategorileri yayımla")
def make_category_published(modeladmin, request, queryset):
    queryset.update(status='1')


@admin.action(description="Seçili kategorileri taslak yap")
def make_category_draft(modeladmin, request, queryset):
    queryset.update(status='0')


# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createdOn', 'updatedOn', 'status')
    list_display_links = ['id', 'name']
    list_filter = ['status']
    ordering = ['id']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    # list_editable = ['status']
    list_per_page = 20
    # special actions
    actions = [make_category_published, make_category_draft]


admin.site.register(Category, CategoryAdmin)


# Posts Actions
@admin.action(description="Seçili yazıları yayınla")
def make_post_published(modeladmin, request, queryset):
    queryset.update(status='1')


@admin.action(description="Seçili yazıları taslak yap")
def make_post_draft(modeladmin, request, queryset):
    queryset.update(status='0')


# Posts Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'createdOn', 'status')
    list_filter = ('status','author')
    list_display_links = ['title']
    ordering = ['id']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    # list_editable = ['status']
    list_per_page = 20
    # special actions
    actions = [make_post_published, make_post_draft]


admin.site.register(Post, PostAdmin)
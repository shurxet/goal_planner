from django.contrib import admin
from goals.models import GoalCategory, GoalComment, Goal


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_deleted')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('is_deleted',)
    readonly_fields = ('created', 'updated',)


@admin.register(Goal)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'category', 'status', 'priority')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority')
    readonly_fields = ('created', 'updated',)


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user')
    list_display_links = ('text',)
    search_fields = ('text',)
    readonly_fields = ('created', 'updated',)

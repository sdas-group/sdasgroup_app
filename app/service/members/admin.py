from django.contrib import admin

from .models import Member
from .models import Publication


@admin.register(Member)
class MembersAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = (
        'full_name',
        'email',
        'description'
    )

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'full_name',
                'email',
                'photo',
                'website',
                'description',
                'type_member',
                'type_member_2',
                'type_member_3',
                'research_interest',
                'active',
                'slug',
            ),
        }),
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = (
        'title',
        'event_of_publication',
        'member',
        'year'
    )

    fieldsets = (
        ('publication item', {
            'fields': (
                'title',
                'event_of_publication',
                'member',
                'author',
                'abstract',
                'year',
                'url_publication',
            ),
        }),
    )

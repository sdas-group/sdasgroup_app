from django.contrib import admin

from .models import HomeInfo
from .models import ProjectInfo
from .models import ServiceInfo
from .models import ResearchLine
from .models import ContactInformation
from .models import Repository
from .models import CourseInfo
from .models import Gallery
from .models import Image


@admin.register(HomeInfo)
class HomeInfoAdmin(admin.ModelAdmin):
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
        'description'
    )

    fieldsets = (
        ('home item', {
            'fields': (
                'title',
                'description',
                'video'
            ),
        }),
    )


@admin.register(ProjectInfo)
class ProjectInfoAdmin(admin.ModelAdmin):
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
        'project',
        'description'
    )

    fieldsets = (
        ('project item', {
            'fields': (
                'project',
                'description',
                'image',
                'url_project',
                'type_project'
            ),
        }),
    )


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
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
        'service',
        'description'
    )

    fieldsets = (
        ('service item', {
            'fields': (
                'service',
                'description'
            ),
        }),
    )


@admin.register(ResearchLine)
class ResearchLineAdmin(admin.ModelAdmin):
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
        'research_line',
        'description',
        'url_research'
    )

    fieldsets = (
        ('research line item', {
            'fields': (
                'research_line',
                'url_research',
                'description',
                'type_line'
            ),
        }),
    )


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = (
        'email',
        'phone'
    )

    fieldsets = (
        ('contact item', {
            'fields': (
                'email',
                'phone'
            ),
        }),
    )


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
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
        'description',
        'type_repository',
    )

    fieldsets = (
        ('repository item', {
            'fields': (
                'title',
                'description',
                'url_repository',
                'year',
                'type_repository',
            ),
        }),
    )


@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
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
        'course',
        'description',
        'type_course',
    )

    fieldsets = (
        ('course and event item', {
            'fields': (
                'course',
                'description',
                'type_course',
                'url_course',
            ),
        }),
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
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
        'description'
    )

    readonly_fields = (
        'slug',
    )

    fieldsets = (
        ('gallery item', {
            'fields': (
                'title',
                'description',
                'slug',
            ),
        }),
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
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
        'id',
        'image',
        'album'
    )

    fieldsets = (
        ('image item', {
            'fields': (
                'image',
                'album',
            ),
        }),
    )

from django.db import models
from django.utils.text import slugify

from .data import REPOSITORY_CHOICES
from .data import COURSE_CHOICES
from .data import LINE_CHOICES
from .data import PROJECT_CHOICES


class HomeInfo(models.Model):
    title = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='title',
    )

    video = models.FileField(
        upload_to='media',
        null=True,
        blank=True,
        verbose_name='video',
    )

    description = models.TextField(
        verbose_name='description',
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Home Item'
        verbose_name_plural = 'Home Items'
        ordering = ('id',)


class ProjectInfo(models.Model):
    project = models.CharField(
        max_length=128,
        verbose_name='project',
    )

    description = models.TextField(
        verbose_name='description',
    )

    image = models.ImageField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='project image',
    )

    url_project = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='project info url',
    )

    type_project = models.PositiveSmallIntegerField(
        choices=PROJECT_CHOICES,
        verbose_name='type of project',
        default=400,
    )

    def __str__(self):
        return self.project

    class Meta:
        verbose_name = 'Project Item'
        verbose_name_plural = 'Project Items'
        ordering = ('id',)


class ServiceInfo(models.Model):
    service = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='service',
    )

    description = models.TextField(
        verbose_name='description',
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Service Item'
        verbose_name_plural = 'Service Items'
        ordering = ('id',)


class ResearchLine(models.Model):
    research_line = models.CharField(
        max_length=128,
        verbose_name='research line',
    )

    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True,
    )

    url_research = models.URLField(
        max_length=200,
        default='No Name',
        verbose_name='research line url',
    )

    type_line = models.PositiveSmallIntegerField(
        choices=LINE_CHOICES,
        verbose_name='type of research line',
        default=300,
    )

    def __str__(self):
        return self.research_line

    class Meta:
        verbose_name = 'Research Line'
        verbose_name_plural = 'Research Lines'
        ordering = ('id',)


class EventInfo(models.Model):
    event = models.CharField(
        max_length=128,
        verbose_name='event',
    )

    description = models.TextField(
        verbose_name='description',
    )

    def __str__(self):
        return self.event

    class Meta:
        verbose_name = 'Event Item'
        verbose_name_plural = 'Event Items'
        ordering = ('id',)


class CourseInfo(models.Model):
    course = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='course',
    )

    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True,
    )

    type_course = models.PositiveSmallIntegerField(
        choices=COURSE_CHOICES,
        verbose_name='type',
        default=200,
    )

    url_course = models.URLField(
        max_length=200,
        default='No Name',
        verbose_name='course url',
    )

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'courses'
        ordering = ('id',)


class ContactInformation(models.Model):
    email = models.CharField(
        max_length=128,
        verbose_name='email',
    )

    phone = models.TextField(
        verbose_name='phone',
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'
        ordering = ('id',)


class Repository(models.Model):
    title = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name='title',
    )

    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True,
    )

    year = models.PositiveSmallIntegerField(
        verbose_name='año',
        null=True,
        blank=True,
    )

    url_repository = models.URLField(
        max_length=200,
        verbose_name='url',
    )

    type_repository = models.PositiveSmallIntegerField(
        choices=REPOSITORY_CHOICES,
        verbose_name='type of repository',
        default=100,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'
        ordering = ('id',)


class Gallery(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='title',
    )

    description = models.TextField(
        verbose_name='description',
    )

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        ordering = ('id',)


class Image(models.Model):
    image = models.ImageField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='image',
    )

    album = models.ForeignKey(
        'groupinformation.Gallery',
        verbose_name='gallery',
        default='No Name Album',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return ''.format(self.id)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('id',)

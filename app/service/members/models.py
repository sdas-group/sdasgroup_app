from django.db import models
from django.core.validators import MinLengthValidator

from .data import MEMBER_CHOICES
from .data import ACTIVE_CHOICES


class Member(models.Model):
    full_name = models.CharField(
        verbose_name='full name',
        max_length=128,
        blank=False,
        validators=[
            MinLengthValidator(3),
        ],
        error_messages={
            'min_length':
                'The field "full name" must have at least %(limit_value)d '
                'characters (it has %(show_value)d).'
        }
    )

    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
    )

    publications_url = models.CharField(
        verbose_name='URL of publications',
        max_length=250,
        blank=True,
    )

    photo = models.ImageField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='photo',
        upload_to='uploads'
    )

    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='website'
    )

    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True,
    )

    type_member = models.PositiveSmallIntegerField(
        choices=MEMBER_CHOICES,
        verbose_name='type of member',
        null=False,
        blank=False
    )

    type_member_2 = models.PositiveSmallIntegerField(
        choices=MEMBER_CHOICES,
        verbose_name='type of member',
        null=True,
        blank=True
    )

    type_member_3 = models.PositiveSmallIntegerField(
        choices=MEMBER_CHOICES,
        verbose_name='type of member',
        null=True,
        blank=True
    )

    research_interest = models.TextField(
        verbose_name='research interest'
    )

    active = models.PositiveSmallIntegerField(
        choices=ACTIVE_CHOICES,
        verbose_name='active',
        null=False,
        blank=False,
        default=200
    )

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ('id',)


class Publication(models.Model):
    title = models.CharField(
        verbose_name='name of publication',
        max_length=200,
        blank=False
    )

    event_of_publication = models.CharField(
        verbose_name='event of publication',
        max_length=200,
        blank=False
    )

    member = models.ForeignKey(
        'members.Member',
        verbose_name='author',
        default='No Name',
        on_delete=models.CASCADE,
    )

    author = models.TextField(
        verbose_name='coauthors',
        default='No Name'
    )

    abstract = models.TextField(
        verbose_name='abstract'
    )

    url_publication = models.URLField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='url of publication'
    )

    year = models.PositiveSmallIntegerField(
        verbose_name='year of publication',
        null=False,
        blank=False
    )

    def __str__(self):
        return self.titles

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ('id',)

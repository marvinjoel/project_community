import datetime
from django.db import models
from django.utils import timezone

from .utils.link_data import LinkData


class Community_info(models.Model):
    title = models.CharField(verbose_name='Título',
                             max_length=300, blank=True, null=True)
    description = models.TextField(
        verbose_name='Descripción', blank=True, null=True)
    r_social1 = models.CharField(
        verbose_name='Facebook', max_length=200, blank=True, null=True)
    r_social2 = models.CharField(
        verbose_name='Instagram', max_length=200, blank=True, null=True)
    r_social3 = models.CharField(
        verbose_name='Linkedin', max_length=200, blank=True, null=True)
    r_social4 = models.CharField(
        verbose_name='Telegram', max_length=200, blank=True, null=True)
    r_social5 = models.CharField(
        verbose_name='Twitter', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Community_info'
        verbose_name_plural = 'Community_infos'
        ordering = ['id']


class Link_Enlace(models.Model):
    whatsapp = models.CharField(
        verbose_name='Whatsapp', max_length=200, blank=True, null=True)
    telegram = models.CharField(
        verbose_name='Telegram', max_length=200, blank=True, null=True)
    discord = models.CharField(
        verbose_name='Discord', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Grupo: {self.whatsapp}'

    class Meta:
        verbose_name = 'Link_Enlace'
        verbose_name_plural = 'Links_Enlaces'
        ordering = ['id']


class EnlacesAPI(models.Model):
    name = models.CharField(max_length=300)
    FIELDNAME = models.URLField()


class Link_Group(models.Model):
    url = models.URLField('group url',
            max_length=250,
            unique=True,
            blank=False,
            null=False
        )
    name = models.CharField('group name', max_length=150, blank=True, null=True)
    description = models.TextField('group description', blank=True, null=True)
    image = models.CharField('group image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created',auto_now_add=True, blank=True)


    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(Link_Group, self).save()

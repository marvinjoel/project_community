# Generated by Django 3.2.8 on 2021-11-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_rename_groups_link_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link_groups',
            name='created',
            field=models.DateField(blank=True, null=True, verbose_name='date published'),
        ),
    ]

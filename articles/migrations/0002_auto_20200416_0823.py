# Generated by Django 3.0.5 on 2020-04-16 08:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articule',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
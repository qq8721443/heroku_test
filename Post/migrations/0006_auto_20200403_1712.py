# Generated by Django 3.0.4 on 2020-04-03 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_post_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-create_dt',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]

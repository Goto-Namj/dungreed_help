# Generated by Django 2.2.3 on 2019-09-24 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dungreed', '0002_test_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='title',
        ),
    ]
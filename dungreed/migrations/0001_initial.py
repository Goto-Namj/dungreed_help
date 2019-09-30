# Generated by Django 2.2.3 on 2019-09-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='.\\dungreed\\static\\image\\item')),
                ('grade', models.CharField(max_length=10)),
                ('use', models.CharField(max_length=20)),
                ('nature', models.CharField(max_length=15)),
                ('data', models.TextField()),
                ('tag', models.CharField(blank=True, max_length=20)),
                ('group', models.CharField(blank=True, max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('state_spc', models.CharField(max_length=25)),
                ('jeison', models.TextField()),
            ],
        ),
    ]

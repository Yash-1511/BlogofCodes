# Generated by Django 3.2.5 on 2021-07-09 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

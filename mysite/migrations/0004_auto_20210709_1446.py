# Generated by Django 3.2.5 on 2021-07-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20210709_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='picture2',
        ),
        migrations.AddField(
            model_name='category',
            name='picture2',
            field=models.ImageField(default=1, upload_to='picture/'),
            preserve_default=False,
        ),
    ]

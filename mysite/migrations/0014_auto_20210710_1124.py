# Generated by Django 3.2.5 on 2021-07-10 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20210710_1120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Squads',
            new_name='Skills2',
        ),
        migrations.AlterModelOptions(
            name='category2',
            options={'verbose_name': 'Skill2', 'verbose_name_plural': 'Skills2'},
        ),
        migrations.RenameField(
            model_name='skills2',
            old_name='player_name',
            new_name='skill_name',
        ),
    ]

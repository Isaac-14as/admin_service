# Generated by Django 2.2.19 on 2023-01-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_part', '0003_maindata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindata',
            name='age_deceased',
            field=models.IntegerField(blank=True, verbose_name='Возраст умершего'),
        ),
    ]

# Generated by Django 3.1 on 2020-09-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
    ]

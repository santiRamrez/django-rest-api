# Generated by Django 4.2.6 on 2023-10-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_alter_book_authors_alter_book_avgevaluation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(db_table='book_authors', to='quickstart.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(db_table='book_categories', to='quickstart.category'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_alter_book_authors_alter_book_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='haveReaded',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='wannaRead',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
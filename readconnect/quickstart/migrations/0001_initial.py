# Generated by Django 4.2.6 on 2023-10-21 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('wannaRead', models.CharField(max_length=100)),
                ('haveReaded', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imgURI', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=20)),
                ('shortDescrip', models.CharField(max_length=255)),
                ('longDescrip', models.TextField()),
                ('pageCount', models.IntegerField()),
                ('publishedDate', models.DateTimeField()),
                ('avgEvaluation', models.DecimalField(decimal_places=1, max_digits=1)),
                ('authors', models.ManyToManyField(to='quickstart.author')),
                ('categories', models.ManyToManyField(to='quickstart.category')),
            ],
        ),
    ]

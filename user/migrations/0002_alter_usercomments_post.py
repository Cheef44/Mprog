# Generated by Django 4.2 on 2023-08-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomments',
            name='post',
            field=models.IntegerField(),
        ),
    ]
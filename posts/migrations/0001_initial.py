# Generated by Django 4.2 on 2023-07-29 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_image', models.ImageField(blank=True, upload_to='D:\\My files\\My projects\\Web\\Python\\Mprog\\mprog\\media/users/%Y/%m/%d/')),
                ('title', models.CharField(max_length=200)),
                ('main_text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='D:\\My files\\My projects\\Web\\Python\\Mprog\\mprog\\media/users/%Y/%m/%d/')),
                ('image1', models.ImageField(blank=True, upload_to='D:\\My files\\My projects\\Web\\Python\\Mprog\\mprog\\media/users/%Y/%m/%d/')),
                ('image2', models.ImageField(blank=True, upload_to='D:\\My files\\My projects\\Web\\Python\\Mprog\\mprog\\media/users/%Y/%m/%d/')),
                ('text', models.TextField()),
                ('file', models.FileField(blank=True, upload_to='D:\\My files\\My projects\\Web\\Python\\Mprog\\mprog\\media/users/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

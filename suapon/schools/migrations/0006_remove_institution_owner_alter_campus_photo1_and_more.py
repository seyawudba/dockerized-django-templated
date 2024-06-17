# Generated by Django 5.0.6 on 2024-06-17 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_campus_photo1_campus_photo2_campus_photo3_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='owner',
        ),
        migrations.AlterField(
            model_name='campus',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images/campus/'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images/campus/'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='images/campus/'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='images/campus/'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='images/campus/'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/logo/'),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.institution')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

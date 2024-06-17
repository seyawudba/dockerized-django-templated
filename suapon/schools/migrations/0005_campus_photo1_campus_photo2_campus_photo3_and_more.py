# Generated by Django 5.0.6 on 2024-06-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_rename_lastname_lead_lastname_alter_lead_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='campus/'),
        ),
        migrations.AddField(
            model_name='campus',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='campus/'),
        ),
        migrations.AddField(
            model_name='campus',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='campus/'),
        ),
        migrations.AddField(
            model_name='campus',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='campus/'),
        ),
        migrations.AddField(
            model_name='campus',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='campus/'),
        ),
        migrations.AddField(
            model_name='institution',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]
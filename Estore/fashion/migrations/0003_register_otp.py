# Generated by Django 5.0.6 on 2024-06-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0002_rename_lname_register_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='otp',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]

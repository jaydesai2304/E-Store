# Generated by Django 5.0.6 on 2024-07-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0009_gadgetproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
# Generated by Django 4.2.4 on 2023-10-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_customuser_managers_remove_customuser_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='contact_number',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.1.2 on 2023-04-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_contact_name_contact_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]

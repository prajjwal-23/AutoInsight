# Generated by Django 4.1.2 on 2023-02-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_category_company_alter_news_date_tag_news_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='companies',
        ),
        migrations.AddField(
            model_name='company',
            name='tags',
            field=models.ManyToManyField(related_name='company', to='home.tag'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_articlepost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

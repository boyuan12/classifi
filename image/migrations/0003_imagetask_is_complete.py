# Generated by Django 4.0.4 on 2022-06-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_imageobject_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetask',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]

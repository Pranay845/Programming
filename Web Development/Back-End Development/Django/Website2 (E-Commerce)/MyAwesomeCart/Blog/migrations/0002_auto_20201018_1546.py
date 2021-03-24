# Generated by Django 3.1.2 on 2020-10-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='pub_date',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='Blog/Images'),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlist', '0002_auto_20190829_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='ulist',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
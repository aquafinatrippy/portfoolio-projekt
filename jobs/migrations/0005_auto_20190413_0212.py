# Generated by Django 2.2 on 2019-04-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20190413_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='too',
            field=models.CharField(default='LINK', max_length=255),
        ),
    ]
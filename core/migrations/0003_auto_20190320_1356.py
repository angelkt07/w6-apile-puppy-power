# Generated by Django 2.1.7 on 2019-03-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190319_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlink',
            name='topic',
            field=models.ManyToManyField(to='core.HashTag'),
        ),
    ]
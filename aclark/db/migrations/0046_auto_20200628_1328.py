# Generated by Django 3.0.7 on 2020-06-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0045_auto_20200615_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Name'),
        ),
    ]

# Generated by Django 3.0.4 on 2020-06-02 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0040_invoice_doc_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskorder',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='time',
            name='task_order',
        ),
        migrations.DeleteModel(
            name='StatementOfWork',
        ),
        migrations.DeleteModel(
            name='TaskOrder',
        ),
    ]
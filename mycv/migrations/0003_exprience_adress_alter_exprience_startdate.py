# Generated by Django 4.2.15 on 2024-09-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0002_exprience'),
    ]

    operations = [
        migrations.AddField(
            model_name='exprience',
            name='adress',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exprience',
            name='startDate',
            field=models.CharField(default='Rabat', max_length=200),
        ),
    ]

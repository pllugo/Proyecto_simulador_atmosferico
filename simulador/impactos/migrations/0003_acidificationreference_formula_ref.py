# Generated by Django 3.2.2 on 2022-05-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impactos', '0002_acidificationreference'),
    ]

    operations = [
        migrations.AddField(
            model_name='acidificationreference',
            name='formula_ref',
            field=models.CharField(default='', max_length=120, verbose_name='formula_ref'),
        ),
    ]

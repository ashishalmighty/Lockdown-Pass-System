# Generated by Django 3.0.5 on 2020-04-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporaterequest',
            name='status',
            field=models.CharField(max_length=15),
        ),
    ]

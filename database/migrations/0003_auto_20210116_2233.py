# Generated by Django 2.2 on 2021-01-16 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210101_0548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='pawn',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='receive',
            options={'managed': True},
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstateObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cad_num', models.CharField()),
                ('shirota', models.CharField()),
                ('dolgota', models.CharField()),
            ],
        ),
    ]

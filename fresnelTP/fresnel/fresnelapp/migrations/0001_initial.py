# Generated by Django 4.2.3 on 2023-08-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='calculo_fresnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia', models.FloatField()),
                ('distancia', models.FloatField()),
            ],
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0011_dutafkip'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliahFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
    ]
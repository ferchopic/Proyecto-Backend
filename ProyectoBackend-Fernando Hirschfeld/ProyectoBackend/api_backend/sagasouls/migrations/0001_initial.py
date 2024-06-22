# Generated by Django 5.0.3 on 2024-05-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SagaSouls',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('año', models.IntegerField()),
                ('company', models.CharField(max_length=128)),
                ('GOTY', models.BooleanField(default=False)),
            ],
        ),
    ]

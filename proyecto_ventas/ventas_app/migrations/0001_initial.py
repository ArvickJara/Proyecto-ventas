# Generated by Django 4.2 on 2023-04-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=12)),
                ('ap', models.CharField(max_length=25)),
                ('am', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=1)),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-12-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('location', models.JSONField()),
            ],
        ),
    ]
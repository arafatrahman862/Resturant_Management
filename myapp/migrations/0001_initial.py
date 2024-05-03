# Generated by Django 5.0.4 on 2024-04-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
    ]

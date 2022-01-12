# Generated by Django 3.0.5 on 2021-12-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField(max_length=800)),
            ],
        ),
    ]

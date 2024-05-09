# Generated by Django 5.0.4 on 2024-05-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_receviemessage_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('address', models.CharField(max_length=150, verbose_name='last name')),
                ('phone', models.CharField(max_length=11, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('age', models.DateTimeField(verbose_name='age')),
                ('condition', models.CharField(choices=[('r', 'ready'), ('unr', 'unready')], max_length=11)),
            ],
        ),
    ]

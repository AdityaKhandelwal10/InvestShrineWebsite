# Generated by Django 3.0.6 on 2020-06-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_remove_user_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('Investor', 'Investor'), ('Entrepreneur', 'Entrepreneur')], default='Investor', max_length=20),
        ),
    ]

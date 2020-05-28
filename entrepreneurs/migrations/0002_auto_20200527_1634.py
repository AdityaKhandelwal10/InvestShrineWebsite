# Generated by Django 3.0.6 on 2020-05-27 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='entrepreneurportfolio',
            name='industry',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entrepreneurs.Industry'),
            preserve_default=False,
        ),
    ]

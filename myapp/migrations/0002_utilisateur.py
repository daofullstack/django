# Generated by Django 2.2.3 on 2019-08-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('compte', models.IntegerField(default=10000)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

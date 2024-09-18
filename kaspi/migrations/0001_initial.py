# Generated by Django 5.0.6 on 2024-08-16 16:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Magazin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=256)),
                ('staff', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MagazineGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaspi.good')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaspi.magazin')),
            ],
        ),
        migrations.AddField(
            model_name='magazin',
            name='goods',
            field=models.ManyToManyField(through='kaspi.MagazineGoods', to='kaspi.good'),
        ),
    ]
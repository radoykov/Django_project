# Generated by Django 5.0.6 on 2024-06-16 17:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0002_alter_vacation_date_created'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('vacation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacations.vacation')),
            ],
        ),
    ]

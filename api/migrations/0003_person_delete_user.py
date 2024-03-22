# Generated by Django 5.0.3 on 2024-03-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_skud_time_user_skud_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Клиент', 'Клиент'), ('Сотрудник', 'Сотрудник')], default='Клиент', max_length=20)),
                ('skud_number', models.IntegerField(default=0)),
                ('skud_direction', models.CharField(choices=[('in', 'in'), ('out', 'out')], default='out', max_length=20)),
                ('skud_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
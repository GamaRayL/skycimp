# Generated by Django 4.2.6 on 2023-10-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='send_date',
        ),
        migrations.AddField(
            model_name='mailing',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата окончания рассылки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата начала рассылки'),
        ),
    ]

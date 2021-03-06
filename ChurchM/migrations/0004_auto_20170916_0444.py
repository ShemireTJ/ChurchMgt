# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChurchM', '0003_auto_20170916_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_type', models.CharField(max_length=16, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Donations',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=32, unique=True)),
                ('event_date', models.DateField()),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='biblereading',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='fund',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='household',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='ministry',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='role',
            name='Remarks',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='ministry',
            field=models.CharField(choices=[('AD', 'Adult'), ('YT', 'Youth'), ('YA', 'Young_Adults'), ('CH', 'Children'), ('OT', 'Other')], default='AD', max_length=2),
        ),
        migrations.AddField(
            model_name='people',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.Household'),
        ),
        migrations.AddField(
            model_name='people',
            name='ministry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.Ministry'),
        ),
        migrations.AddField(
            model_name='people',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.Role'),
        ),
    ]

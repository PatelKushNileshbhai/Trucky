# Generated by Django 3.1.7 on 2021-03-24 12:08

import appuser.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0002_auto_20210323_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='seek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_weight', models.IntegerField()),
                ('rate', models.IntegerField(null=True)),
                ('typeof_vehicle', models.CharField(max_length=20, null=True)),
                ('nameof_goods', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('s_dest_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seek_de', to='appuser.city')),
                ('s_pickup_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seek_pi', to='appuser.city')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='provide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_weight', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('total_capacity', models.IntegerField()),
                ('numberplate_no', models.CharField(max_length=10, validators=[appuser.models.num_plate])),
                ('permits', models.CharField(max_length=20, null=True)),
                ('typeof_vehicle', models.CharField(max_length=20)),
                ('typeof_payment', models.CharField(max_length=20, null=True)),
                ('p_dest_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_de', to='appuser.city')),
                ('p_pickup_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_pi', to='appuser.city')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('provider_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appuser.provide')),
                ('seeker_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appuser.seek')),
            ],
        ),
    ]

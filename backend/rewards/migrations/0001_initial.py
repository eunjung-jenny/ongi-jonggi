# Generated by Django 2.1.15 on 2020-08-02 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('max_vol', models.IntegerField()),
                ('net_price', models.IntegerField()),
                ('expire_date', models.DateTimeField()),
                ('success', models.BooleanField(null=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facility_rewards', to='accounts.Facility')),
            ],
        ),
    ]

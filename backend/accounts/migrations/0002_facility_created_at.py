# Generated by Django 2.1.15 on 2020-07-31 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
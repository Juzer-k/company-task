# Generated by Django 4.1.1 on 2022-09-22 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtelplans', '0002_alter_buyplan_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyplan',
            name='data',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyplan',
            name='roaming',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyplan',
            name='sms',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='buyplan',
            name='subscription',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

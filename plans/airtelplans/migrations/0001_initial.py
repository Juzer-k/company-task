# Generated by Django 4.1.1 on 2022-09-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('data', models.CharField(max_length=20)),
                ('sms', models.IntegerField()),
                ('roaming', models.CharField(max_length=20)),
                ('subscription', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('data', models.CharField(max_length=20)),
                ('sms', models.IntegerField()),
                ('roaming', models.CharField(max_length=20)),
                ('subscription', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=20)),
            ],
        ),
    ]
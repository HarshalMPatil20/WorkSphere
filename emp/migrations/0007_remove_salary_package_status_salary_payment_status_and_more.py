# Generated by Django 4.2 on 2023-04-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='package_status',
        ),
        migrations.AddField(
            model_name='salary',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='salary',
            name='annual_package',
            field=models.CharField(max_length=200),
        ),
    ]

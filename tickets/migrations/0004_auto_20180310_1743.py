# Generated by Django 2.0 on 2018-03-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180310_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'Reverted'), (2, 'Closed'), (3, 'Submitted')], default=3, max_length=1),
        ),
    ]
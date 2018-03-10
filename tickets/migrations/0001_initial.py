# Generated by Django 2.0 on 2018-03-10 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('patient_name', models.CharField(max_length=50)),
                ('insurance', models.CharField(max_length=100)),
                ('issue', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('date_created', models.DateField(auto_now=True)),
                ('escalate_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
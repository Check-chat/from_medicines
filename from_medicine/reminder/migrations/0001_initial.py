# Generated by Django 2.1.7 on 2020-05-18 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noti_Prescription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='remider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noti_Prescription.Prescription')),
            ],
        ),
    ]
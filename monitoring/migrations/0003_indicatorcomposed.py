# Generated by Django 3.0.4 on 2020-03-22 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0002_indicatorcomposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorComposed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.IndicatorComposition')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.Indicator')),
            ],
        ),
    ]
# Generated by Django 2.2.3 on 2020-02-04 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20200204_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAdmin',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rango.Page')),
            ],
            bases=('rango.page',),
        ),
    ]
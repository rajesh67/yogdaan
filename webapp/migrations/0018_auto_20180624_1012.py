# Generated by Django 2.0 on 2018-06-24 04:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20180620_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2018, 6, 24, 10, 12, 26, 393387))),
                ('offers_file', models.FileField(upload_to='get_upload_path')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offerUpdate', to='webapp.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 24, 10, 12, 26, 409018)),
        ),
    ]

# Generated by Django 2.0 on 2018-06-12 12:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0010_auto_20180612_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StoreBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='offer',
            name='users',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 12, 18, 17, 50, 192382)),
        ),
        migrations.AddField(
            model_name='offerbookmark',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Offer'),
        ),
        migrations.AddField(
            model_name='offerbookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
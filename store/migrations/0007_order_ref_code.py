# Generated by Django 2.2.4 on 2019-08-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20190824_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='1234', max_length=20),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.4 on 2021-08-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_rename_crated_sale_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
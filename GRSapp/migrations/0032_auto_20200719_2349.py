# Generated by Django 3.0.8 on 2020-07-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0031_auto_20200719_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='hearts',
            field=models.IntegerField(default=31),
        ),
        migrations.AlterField(
            model_name='camera',
            name='rating',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='headset',
            name='hearts',
            field=models.IntegerField(default=17),
        ),
        migrations.AlterField(
            model_name='headset',
            name='rating',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='hearts',
            field=models.IntegerField(default=16),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='hearts',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='powerbank',
            name='hearts',
            field=models.IntegerField(default=13),
        ),
        migrations.AlterField(
            model_name='powerbank',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='hearts',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='refrigerator',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='television',
            name='hearts',
            field=models.IntegerField(default=14),
        ),
        migrations.AlterField(
            model_name='television',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='washingmachine',
            name='hearts',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='washingmachine',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
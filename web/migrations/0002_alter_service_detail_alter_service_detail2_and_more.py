# Generated by Django 4.1.7 on 2023-04-21 06:19

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='detail2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image2',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='sub_head',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='sub_head2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-14 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_postimg_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimg',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.categoryimg'),
        ),
    ]

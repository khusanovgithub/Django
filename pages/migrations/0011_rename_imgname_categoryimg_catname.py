# Generated by Django 4.0.4 on 2022-06-14 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_postimg_cat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryimg',
            old_name='imgName',
            new_name='catName',
        ),
    ]

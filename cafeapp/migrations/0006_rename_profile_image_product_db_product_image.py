# Generated by Django 5.0 on 2024-01-03 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0005_remove_login_db_email_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_db',
            old_name='profile_image',
            new_name='product_image',
        ),
    ]

# Generated by Django 5.1 on 2024-12-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_rename_des_categorys_feature_remove_categorys_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='companys',
            name='c_info',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

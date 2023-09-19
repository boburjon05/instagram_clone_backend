# Generated by Django 4.2 on 2023-09-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_auth_status_user_auth_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('CODE_VERIFIED', 'CODE_VERIFIED'), ('DONE', 'DONE'), ('PHOTO_DONE', 'PHOTO_DONE')], default='NEW', max_length=31),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_comment_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

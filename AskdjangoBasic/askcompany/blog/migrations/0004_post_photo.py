# Generated by Django 3.2.5 on 2021-07-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]

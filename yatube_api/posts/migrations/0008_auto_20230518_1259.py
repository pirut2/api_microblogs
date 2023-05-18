# Generated by Django 3.2.16 on 2023-05-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_rename_author_follow_following'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ['following']},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date']},
        ),
    ]

# Generated by Django 3.2.16 on 2023-05-18 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_follow_unique_user_following'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date']},
        ),
    ]

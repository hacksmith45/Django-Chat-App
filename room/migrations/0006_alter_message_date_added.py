# Generated by Django 4.2.2 on 2023-06-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_alter_message_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 4.2.11 on 2024-04-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello_world", "0004_alter_comment_options_post_excerpt_post_updated_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="name",
            field=models.CharField(default="test", max_length=200),
        ),
    ]

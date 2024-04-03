# Generated by Django 4.2.11 on 2024-04-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello_world", "0003_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment", options={"ordering": ["created_on"]},
        ),
        migrations.AddField(
            model_name="post", name="excerpt", field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
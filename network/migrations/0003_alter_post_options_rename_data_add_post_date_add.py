# Generated by Django 4.0.4 on 2022-05-30 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_post_options_rename_publish_post_data_add'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date_add',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_add',
            new_name='date_add',
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-27 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210327_0232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ()},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='alterado',
            new_name='altered',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='conteudo',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='criado',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publicado',
            new_name='published',
        ),
    ]

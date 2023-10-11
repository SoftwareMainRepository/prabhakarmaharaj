# Generated by Django 4.2.4 on 2023-09-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typesofpuja',
            name='name',
        ),
        migrations.AddField(
            model_name='typesofpuja',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='typesofpuja',
            name='description',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]
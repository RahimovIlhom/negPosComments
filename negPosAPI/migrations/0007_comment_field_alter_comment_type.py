# Generated by Django 4.2 on 2023-05-02 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negPosAPI', '0006_alter_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='field',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
# Generated by Django 4.2 on 2023-04-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negPosAPI', '0002_comment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
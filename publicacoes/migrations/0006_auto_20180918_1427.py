# Generated by Django 2.1 on 2018-09-18 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0005_auto_20180918_1413'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categoria',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='publicacao',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
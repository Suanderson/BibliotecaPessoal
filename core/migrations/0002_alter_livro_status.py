# Generated by Django 5.1.2 on 2025-02-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='status',
            field=models.CharField(choices=[('le', 'Lendo'), ('li', 'Lido'), ('de', 'Deseja-se')], max_length=2, verbose_name='Status'),
        ),
    ]

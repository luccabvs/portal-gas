# Generated by Django 4.0.1 on 2022-07-31 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_perfil_nome_exibicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='responsavel',
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='responsavel',
        ),
    ]
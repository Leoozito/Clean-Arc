# Generated by Django 3.2.12 on 2023-11-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estampagens', '0002_alter_estampagens_ae'),
    ]

    operations = [
        migrations.AddField(
            model_name='estampagens',
            name='status',
            field=models.CharField(choices=[('CRIADO', 'Criado'), ('INICIADO', 'Iniciado'), ('EM_ESTAMPAGEM', 'Em_Estampagem'), ('CONCLUIDO', 'Concluido'), ('CANCELADO', 'Cancelado')], default='OPEN', max_length=20),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-29 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0002_auto_20190929_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuestionario',
            old_name='nss',
            new_name='nss_paciente',
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='estado_civil',
            field=models.CharField(choices=[('Casado', 'Casado'), ('Soltero', 'Sotero'), ('Viudo', 'Viudo'), ('Divorceado', 'Divorciado'), ('Union libre', 'Union Libre')], max_length=15),
        ),
    ]
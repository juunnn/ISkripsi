# Generated by Django 2.0 on 2017-12-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_bimbinganproposal_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='npm',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Mahasiswa'),
        ),
    ]
# Generated by Django 2.0 on 2017-12-24 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0008_auto_20171223_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminarproposal',
            name='proposal',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='propSid', to='proposal.Proposal'),
        ),
    ]
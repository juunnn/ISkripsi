# Generated by Django 2.0 on 2017-12-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_proposal_lolos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminarproposal',
            name='masabimbingan',
            field=models.BooleanField(default=True),
        ),
    ]
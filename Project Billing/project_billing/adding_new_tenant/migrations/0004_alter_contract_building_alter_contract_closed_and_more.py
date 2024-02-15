# Generated by Django 4.2.5 on 2024-02-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adding_new_tenant', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='building',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='closed',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_beginning',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_end',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_of_agreement',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='in_work',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='landlord',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='lot',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='main_agreement',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='number_of_agreement',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='number_of_contract',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='tax_for_ad',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='tenant',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='tenant_ps',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='type_of_contract',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]

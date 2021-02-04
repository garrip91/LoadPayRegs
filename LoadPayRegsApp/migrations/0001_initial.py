# Generated by Django 3.1.5 on 2021-02-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='docs/')),
            ],
        ),
        migrations.CreateModel(
            name='TableColumns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(blank=True, max_length=255, null=True, verbose_name='Организация')),
                ('material_assigning', models.CharField(blank=True, max_length=255, null=True, verbose_name='Назначение материала')),
                ('account_purpose', models.CharField(blank=True, max_length=255, null=True, verbose_name='Назначение счёта')),
                ('contract_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='№ договора')),
                ('contract_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='Сумма по договору')),
                ('paid1', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='Оплачено')),
                ('account_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='№ счёта')),
                ('account_date', models.DateField(blank=True, null=True, verbose_name='Дата счёта')),
                ('accounts_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='Сумма по счётам')),
                ('for_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='В оплату')),
                ('payment_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='Остаток по оплате')),
                ('paid2', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='Оплачено')),
                ('remainder', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True, verbose_name='Остаток')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Примечание')),
            ],
        ),
    ]
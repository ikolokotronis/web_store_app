# Generated by Django 4.0 on 2021-12-10 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_order_amount_payed_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount_payed',
            new_name='amount_paid',
        ),
    ]
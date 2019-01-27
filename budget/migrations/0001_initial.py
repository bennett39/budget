# Generated by Django 2.1.5 on 2019-01-27 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('time_refreshed', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_accountid', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=140)),
                ('nickname', models.CharField(max_length=140)),
                ('account_type', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccountGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=140)),
                ('long_item', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signed_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField()),
                ('pc_transaction_id', models.CharField(max_length=60)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_account', to='budget.BankAccount')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_category', to='budget.Category')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_item', to='budget.Item')),
            ],
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='account_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_group', to='budget.BankAccountGroup'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_institution', to='budget.Institution'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='balance',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_balance', to='budget.BankAccount'),
        ),
    ]

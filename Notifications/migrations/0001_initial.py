# Generated by Django 5.1.2 on 2024-10-22 11:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paid', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContributionPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('period_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContributionReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contribution_frequency', models.CharField(choices=[('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('contribution_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_periods', models.PositiveIntegerField(help_text='Total number of contribution periods')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(choices=[('SIGNUP', 'Sign Up'), ('LOGIN', 'Login'), ('KYC_CONFIRMED', 'KYC Confirmed'), ('PAYMENT_SUCCESSFUL', 'Payment Successful'), ('PAYMENT_FAILED', 'Payment Failed'), ('CONTRIBUTION_SUCCESSFUL', 'Contribution Successful'), ('CYCLE_PAYMENT_RECEIVED', 'Cycle Payment Received'), ('FAILED_PAYMENT', 'Failed Payment'), ('WALLET_WITHDRAWAL', 'Wallet Withdrawal Successful'), ('WALLET_DEPOSIT', 'Wallet Deposit Successful'), ('GROUP_JOIN', 'Group Join Successful'), ('GROUP_REMOVAL', 'Group Removal Alert'), ('GROUP_INVITATION', 'Group Invitation Received')], max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email_sent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

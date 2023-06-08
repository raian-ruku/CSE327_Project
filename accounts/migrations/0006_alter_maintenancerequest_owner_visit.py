# Generated by Django 4.1.7 on 2023-05-31 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_description_maintenancerequest_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_requests', to='accounts.webuser'),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('nid_number', models.CharField(max_length=20)),
                ('visit_date', models.DateField()),
                ('visit_time', models.TimeField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.apartment')),
            ],
        ),
    ]

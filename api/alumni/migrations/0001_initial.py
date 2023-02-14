# Generated by Django 4.1.4 on 2023-01-31 10:36

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
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('rv_email', models.CharField(max_length=100, null=True)),
                ('branch', models.CharField(max_length=50, null=True)),
                ('year_joined', models.DateField(null=True)),
                ('year_passed', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alumnus_details', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alumni',
            },
        ),
        migrations.CreateModel(
            name='Placements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_profile', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=20, null=True)),
                ('ctc', models.CharField(max_length=10, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('alumnus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumni.alumni')),
            ],
            options={
                'db_table': 'placements',
            },
        ),
        migrations.CreateModel(
            name='Internships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=10, null=True)),
                ('stipend', models.CharField(max_length=10, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('alumnus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumni.alumni')),
            ],
            options={
                'db_table': 'internships',
            },
        ),
        migrations.CreateModel(
            name='HigherStudies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('start_year', models.DateField(null=True)),
                ('end_year', models.DateField(null=True)),
                ('alumnus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumni.alumni')),
            ],
            options={
                'db_table': 'higher_studies',
            },
        ),
    ]

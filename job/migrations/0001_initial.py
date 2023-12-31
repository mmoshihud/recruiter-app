# Generated by Django 4.2.5 on 2023-10-09 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('resume_url', models.URLField()),
                ('application_date', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('Accounting', 'Accounting'), ('Administrative', 'Administrative'), ('Arts & Entertainment', 'Arts & Entertainment'), ('Consulting', 'Consulting'), ('Customer Service', 'Customer Service'), ('Design', 'Design'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('Finance', 'Finance'), ('Health & Fitness', 'Health & Fitness'), ('Hospitality', 'Hospitality'), ('Human Resources', 'Human Resources'), ('IT', 'IT & Telecommunication'), ('Law', 'Law & Legal'), ('Manufacturing', 'Manufacturing'), ('Marketing', 'Marketing'), ('Media & Communication', 'Media & Communication'), ('Medical', 'Medical'), ('Retail', 'Retail'), ('Sales', 'Sales'), ('Science', 'Science'), ('Social Services', 'Social Services'), ('Transportation', 'Transportation')], max_length=255)),
                ('vacancy', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('job_poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=10)),
                ('feedback_description', models.TextField()),
                ('feedback_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.application')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=10)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job'),
        ),
    ]
